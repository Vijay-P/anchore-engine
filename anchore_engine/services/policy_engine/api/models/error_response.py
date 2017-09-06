# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ErrorResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, type=None, message=None):
        """
        ErrorResponse - a model defined in Swagger

        :param code: The code of this ErrorResponse.
        :type code: int
        :param type: The type of this ErrorResponse.
        :type type: str
        :param message: The message of this ErrorResponse.
        :type message: str
        """
        self.swagger_types = {
            'code': int,
            'type': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'type': 'type',
            'message': 'message'
        }

        self._code = code
        self._type = type
        self._message = message

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorResponse of this ErrorResponse.
        :rtype: ErrorResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def code(self):
        """
        Gets the code of this ErrorResponse.

        :return: The code of this ErrorResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorResponse.

        :param code: The code of this ErrorResponse.
        :type code: int
        """

        self._code = code

    @property
    def type(self):
        """
        Gets the type of this ErrorResponse.

        :return: The type of this ErrorResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ErrorResponse.

        :param type: The type of this ErrorResponse.
        :type type: str
        """

        self._type = type

    @property
    def message(self):
        """
        Gets the message of this ErrorResponse.

        :return: The message of this ErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorResponse.

        :param message: The message of this ErrorResponse.
        :type message: str
        """

        self._message = message

