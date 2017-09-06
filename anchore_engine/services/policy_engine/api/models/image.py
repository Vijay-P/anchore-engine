# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Image(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, digest=None, user_id=None, state=None, distro_namespace=None, created_at=None, last_modified=None, tags=None):
        """
        Image - a model defined in Swagger

        :param id: The id of this Image.
        :type id: str
        :param digest: The digest of this Image.
        :type digest: str
        :param user_id: The user_id of this Image.
        :type user_id: str
        :param state: The state of this Image.
        :type state: str
        :param distro_namespace: The distro_namespace of this Image.
        :type distro_namespace: str
        :param created_at: The created_at of this Image.
        :type created_at: datetime
        :param last_modified: The last_modified of this Image.
        :type last_modified: datetime
        :param tags: The tags of this Image.
        :type tags: List[str]
        """
        self.swagger_types = {
            'id': str,
            'digest': str,
            'user_id': str,
            'state': str,
            'distro_namespace': str,
            'created_at': datetime,
            'last_modified': datetime,
            'tags': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'digest': 'digest',
            'user_id': 'user_id',
            'state': 'state',
            'distro_namespace': 'distro_namespace',
            'created_at': 'created_at',
            'last_modified': 'last_modified',
            'tags': 'tags'
        }

        self._id = id
        self._digest = digest
        self._user_id = user_id
        self._state = state
        self._distro_namespace = distro_namespace
        self._created_at = created_at
        self._last_modified = last_modified
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Image of this Image.
        :rtype: Image
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self):
        """
        Gets the id of this Image.

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.

        :param id: The id of this Image.
        :type id: str
        """

        self._id = id

    @property
    def digest(self):
        """
        Gets the digest of this Image.

        :return: The digest of this Image.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """
        Sets the digest of this Image.

        :param digest: The digest of this Image.
        :type digest: str
        """

        self._digest = digest

    @property
    def user_id(self):
        """
        Gets the user_id of this Image.

        :return: The user_id of this Image.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Image.

        :param user_id: The user_id of this Image.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def state(self):
        """
        Gets the state of this Image.
        State of the image in the policy evaluation system

        :return: The state of this Image.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Image.
        State of the image in the policy evaluation system

        :param state: The state of this Image.
        :type state: str
        """
        allowed_values = ["failed", "initializing", "analyzing", "analyzed"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def distro_namespace(self):
        """
        Gets the distro_namespace of this Image.
        The namespace identifier for this image for purposes of CVE matches, etc

        :return: The distro_namespace of this Image.
        :rtype: str
        """
        return self._distro_namespace

    @distro_namespace.setter
    def distro_namespace(self, distro_namespace):
        """
        Sets the distro_namespace of this Image.
        The namespace identifier for this image for purposes of CVE matches, etc

        :param distro_namespace: The distro_namespace of this Image.
        :type distro_namespace: str
        """

        self._distro_namespace = distro_namespace

    @property
    def created_at(self):
        """
        Gets the created_at of this Image.
        The timestamp on when this image record was created, not the image itself

        :return: The created_at of this Image.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Image.
        The timestamp on when this image record was created, not the image itself

        :param created_at: The created_at of this Image.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def last_modified(self):
        """
        Gets the last_modified of this Image.
        Time the image record in this service was last updated

        :return: The last_modified of this Image.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this Image.
        Time the image record in this service was last updated

        :param last_modified: The last_modified of this Image.
        :type last_modified: datetime
        """

        self._last_modified = last_modified

    @property
    def tags(self):
        """
        Gets the tags of this Image.
        List of tags currently applied to the image. Updated by new tag events. Similarly scoped by the user_id

        :return: The tags of this Image.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Image.
        List of tags currently applied to the image. Updated by new tag events. Similarly scoped by the user_id

        :param tags: The tags of this Image.
        :type tags: List[str]
        """

        self._tags = tags

