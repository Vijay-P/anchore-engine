# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, gate=None, trigger=None, action=None, params=None):
        """
        PolicyRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'gate': 'str',
            'trigger': 'str',
            'action': 'str',
            'params': 'list[PolicyRuleParams]'
        }

        self.attribute_map = {
            'id': 'id',
            'gate': 'gate',
            'trigger': 'trigger',
            'action': 'action',
            'params': 'params'
        }

        self._id = id
        self._gate = gate
        self._trigger = trigger
        self._action = action
        self._params = params

    @property
    def id(self):
        """
        Gets the id of this PolicyRule.

        :return: The id of this PolicyRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PolicyRule.

        :param id: The id of this PolicyRule.
        :type: str
        """

        self._id = id

    @property
    def gate(self):
        """
        Gets the gate of this PolicyRule.

        :return: The gate of this PolicyRule.
        :rtype: str
        """
        return self._gate

    @gate.setter
    def gate(self, gate):
        """
        Sets the gate of this PolicyRule.

        :param gate: The gate of this PolicyRule.
        :type: str
        """
        if gate is None:
            raise ValueError("Invalid value for `gate`, must not be `None`")

        self._gate = gate

    @property
    def trigger(self):
        """
        Gets the trigger of this PolicyRule.

        :return: The trigger of this PolicyRule.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """
        Sets the trigger of this PolicyRule.

        :param trigger: The trigger of this PolicyRule.
        :type: str
        """
        if trigger is None:
            raise ValueError("Invalid value for `trigger`, must not be `None`")

        self._trigger = trigger

    @property
    def action(self):
        """
        Gets the action of this PolicyRule.

        :return: The action of this PolicyRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PolicyRule.

        :param action: The action of this PolicyRule.
        :type: str
        """
        allowed_values = ["GO", "STOP", "WARN"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def params(self):
        """
        Gets the params of this PolicyRule.

        :return: The params of this PolicyRule.
        :rtype: list[PolicyRuleParams]
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this PolicyRule.

        :param params: The params of this PolicyRule.
        :type: list[PolicyRuleParams]
        """

        self._params = params

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
