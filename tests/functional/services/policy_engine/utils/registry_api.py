from tests.functional.services.utils import http_utils


def post_registry(
    registry: str,
    registry_name: str,
    registry_pass: str,
    registry_type: str,
    registry_user: str,
    registry_verify: bool,
) -> http_utils.APIResponse:
    registry_payload = {
        "registry": registry,
        "registry_name": registry_name,
        "registry_pass": registry_pass,
        "registry_type": registry_type,
        "registry_user": registry_user,
        "registry_verify": registry_verify,
    }
    for k, v in registry_payload.items():
        if v == "" or isinstance(v, type(None)):
            raise ValueError("Cannot post registry without %s" % k)
    add_registry_resp = http_utils.http_post(["registries"], registry_payload)
    if add_registry_resp.code != 200:
        raise http_utils.RequestFailedError(
            add_registry_resp.url, add_registry_resp.code, add_registry_resp.body
        )
    return add_registry_resp


def delete_registry(registry_name: str) -> http_utils.APIResponse:
    if not registry_name:
        raise ValueError("Cannot delete registry without registry_name")
    remove_resp = http_utils.http_del(["registries", registry_name])
    if remove_resp.code != 200:
        raise http_utils.RequestFailedError(
            remove_resp.url,
            remove_resp.code,
            "" if not hasattr(remove_resp, "body") else remove_resp.body,
        )
    return remove_resp
