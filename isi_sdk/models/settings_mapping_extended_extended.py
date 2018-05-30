# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SettingsMappingExtendedExtended(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain': 'str',
        'id': 'str',
        'mapping': 'str',
        'type': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'id': 'id',
        'mapping': 'mapping',
        'type': 'type'
    }

    def __init__(self, domain=None, id=None, mapping=None, type=None):  # noqa: E501
        """SettingsMappingExtendedExtended - a model defined in Swagger"""  # noqa: E501

        self._domain = None
        self._id = None
        self._mapping = None
        self._type = None
        self.discriminator = None

        self.domain = domain
        if id is not None:
            self.id = id
        self.mapping = mapping
        self.type = type

    @property
    def domain(self):
        """Gets the domain of this SettingsMappingExtendedExtended.  # noqa: E501

        The FQDN of the source domain to map.  # noqa: E501

        :return: The domain of this SettingsMappingExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SettingsMappingExtendedExtended.

        The FQDN of the source domain to map.  # noqa: E501

        :param domain: The domain of this SettingsMappingExtendedExtended.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def id(self):
        """Gets the id of this SettingsMappingExtendedExtended.  # noqa: E501


        :return: The id of this SettingsMappingExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingsMappingExtendedExtended.


        :param id: The id of this SettingsMappingExtendedExtended.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def mapping(self):
        """Gets the mapping of this SettingsMappingExtendedExtended.  # noqa: E501

        The FQDN of destination domain to map to.  # noqa: E501

        :return: The mapping of this SettingsMappingExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this SettingsMappingExtendedExtended.

        The FQDN of destination domain to map to.  # noqa: E501

        :param mapping: The mapping of this SettingsMappingExtendedExtended.  # noqa: E501
        :type: str
        """
        if mapping is None:
            raise ValueError("Invalid value for `mapping`, must not be `None`")  # noqa: E501

        self._mapping = mapping

    @property
    def type(self):
        """Gets the type of this SettingsMappingExtendedExtended.  # noqa: E501

        The authentication provider type.  # noqa: E501

        :return: The type of this SettingsMappingExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SettingsMappingExtendedExtended.

        The authentication provider type.  # noqa: E501

        :param type: The type of this SettingsMappingExtendedExtended.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ad", "local", "nis", "ldap"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingsMappingExtendedExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
