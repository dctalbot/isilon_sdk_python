# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateCompatibilitiesClassActiveItemResponseSplit(object):
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
        'id': 'int',
        'name': 'str',
        'tier_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tier_name': 'tier_name'
    }

    def __init__(self, id=None, name=None, tier_name=None):  # noqa: E501
        """CreateCompatibilitiesClassActiveItemResponseSplit - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._tier_name = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.tier_name = tier_name

    @property
    def id(self):
        """Gets the id of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501

        The nodepool id that will be split  # noqa: E501

        :return: The id of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateCompatibilitiesClassActiveItemResponseSplit.

        The nodepool id that will be split  # noqa: E501

        :param id: The id of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501

        The nodepool name that will be split  # noqa: E501

        :return: The name of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCompatibilitiesClassActiveItemResponseSplit.

        The nodepool name that will be split  # noqa: E501

        :param name: The name of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tier_name(self):
        """Gets the tier_name of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501

        A message explaining how the nodepools tier membership will change.  # noqa: E501

        :return: The tier_name of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501
        :rtype: str
        """
        return self._tier_name

    @tier_name.setter
    def tier_name(self, tier_name):
        """Sets the tier_name of this CreateCompatibilitiesClassActiveItemResponseSplit.

        A message explaining how the nodepools tier membership will change.  # noqa: E501

        :param tier_name: The tier_name of this CreateCompatibilitiesClassActiveItemResponseSplit.  # noqa: E501
        :type: str
        """
        if tier_name is None:
            raise ValueError("Invalid value for `tier_name`, must not be `None`")  # noqa: E501

        self._tier_name = tier_name

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
        if not isinstance(other, CreateCompatibilitiesClassActiveItemResponseSplit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
