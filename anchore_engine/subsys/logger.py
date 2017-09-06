import inspect
import sys
import threading
from twisted.python import log
from functools import wraps

# Configure a standard python logger for stdout use during bootstrap
import logging

bootstrap_logger = None
bootstrap_logger_enabled = False

log_level_map = {
    'FATAL': 0,
    'ERROR': 1,
    'WARN': 2,
    'INFO': 3,
    'DEBUG': 4,
    'SPEW': 99
}
log_level = None
_log_to_db = None
_log_to_stdout = False

def enable_bootstrap_logging(name_prefix=None):
    """
    Turn on the bootstrap logger, which provides basic stdout logs until the main twisted logger is online and ready.

    :param name_prefix:
    :return:
    """
    global bootstrap_logger_enabled, bootstrap_logger, log_level

    if log_level:
        level = filter(lambda x: x[1] == log_level, log_level_map.items())
        # now select the right element of the tuple
        if level:
            level = level[0][0]
            if level == 'SPEW':
                level = 'DEBUG'
    else:
        level = 'INFO'

    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s - %(message)s")
    logname = name_prefix + '_bootstrap' if name_prefix else 'bootstrap'
    bootstrap_logger = logging.getLogger(logname)
    bootstrap_logger_enabled = True


def disable_bootstrap_logging():
    global bootstrap_logger_enabled, bootstrap_logger
    logging.root.handlers = []
    bootstrap_logger_enabled = False
    bootstrap_logger = None


# A decorator to duplicate a log message to a standard python log gated by the bootstrap enabled flag
def bootstrap_logger_intercept(level):
    def outer_wrapper(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            global bootstrap_logger_enabled
            if bootstrap_logger_enabled:
                if level == 'EXCEPTION':
                    bootstrap_logger.exception(msg=args[0])
                else:
                    bootstrap_logger.log(level=level, msg=args[0])
            return f(*args, **kwds)
        return wrapper
    return outer_wrapper


def _msg(msg_string, msg_log_level='INFO'):
    global log_level, log_level_map, _log_to_stdout, _log_to_db

    if log_level == None:
        log_level = log_level_map['INFO']

    if log_level_map[msg_log_level] <= log_level:
        tname = threading.current_thread().getName()
        caller_file = "-"
        caller_name = "-"
        try:
            current_frame = inspect.currentframe()
            outer_frame = inspect.getouterframes(current_frame, 3)
            frame = inspect.stack()[3]
            module = inspect.getmodule(frame[0])
            caller_file = module.__name__
            caller_name = outer_frame[3][3]
        except Exception as err:
            pass

        themsg = "[" + caller_file + "/" + caller_name + "()] [" + msg_log_level + "] " + msg_string

        log.msg("[" + str(tname) + "] " + themsg)

        if _log_to_stdout:
            sys.stderr.write("[" + str(tname) + "] " + themsg + '\n')

        if _log_to_db:
            # only store logs of higher severity than WARN
            if log_level_map[msg_log_level] < log_level_map['ERROR']:
                try:
                    import anchore_engine.configuration.localconfig

                    localconfig = anchore_engine.configuration.localconfig.get_config()
                    myservices = localconfig['myservices']
                    system_user_auth = localconfig['system_user_auth']
                    hostId = localconfig['host_id']

                    if 'catalog' not in myservices:
                        import anchore_engine.clients.catalog

                        # call the catalog via client to log the error

                        rc = anchore_engine.clients.catalog.add_event(system_user_auth, hostId, ','.join(myservices),
                                                                      'FATAL', str(themsg))
                    else:
                        import anchore_engine.services.common
                        import anchore_engine.db.db_eventlog

                        # log directly to DB if we're the catalog
                        with anchore_engine.services.common.session_scope() as dbsession:
                            anchore_engine.db.db_eventlog.add(hostId, ','.join(myservices), str(themsg), 'FATAL', {},
                                                              session=dbsession)

                except Exception as err:
                    # we're in the logger
                    log.msg("exception in logger: " + str(err))


#@bootstrap_logger_intercept(logging.DEBUG)
def spew(msg_string):
    return (_msg(msg_string, msg_log_level='SPEW'))


@bootstrap_logger_intercept(logging.DEBUG)
def debug(msg_string):
    return (_msg(msg_string, msg_log_level='DEBUG'))


@bootstrap_logger_intercept(logging.INFO)
def info(msg_string):
    return (_msg(msg_string, msg_log_level='INFO'))


@bootstrap_logger_intercept(logging.WARN)
def warn(msg_string):
    return (_msg(msg_string, msg_log_level='WARN'))


@bootstrap_logger_intercept(logging.ERROR)
def error(msg_string):
    return (_msg(msg_string, msg_log_level='ERROR'))


@bootstrap_logger_intercept('EXCEPTION')
def exception(msg_string):
    import traceback
    traceback.print_exc()
    return (_msg(msg_string, msg_log_level='ERROR'))


@bootstrap_logger_intercept(logging.FATAL)
def fatal(msg_string):
    return (_msg(msg_string, msg_log_level='FATAL'))


def set_log_level(new_log_level, log_to_stdout=False, log_to_db=False):
    """
    Set log level for twisted logging
    :param new_log_level: a string name of log level, e.g. 'INFO', 'DEBUG'
    :param log_to_stdout:
    :param log_to_db:
    :return:
    """
    global log_level, log_level_map, _log_to_stdout, _log_to_db

    if new_log_level in log_level_map:
        log_level = log_level_map[new_log_level]

    _log_to_stdout = log_to_stdout
    _log_to_db = log_to_db

