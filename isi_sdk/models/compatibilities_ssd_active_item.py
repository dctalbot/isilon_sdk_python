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


class CompatibilitiesSsdActiveItem(object):
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
        'assess': 'bool',
        'class_1': 'str',
        'class_2': 'str'
    }

    attribute_map = {
        'assess': 'assess',
        'class_1': 'class_1',
        'class_2': 'class_2'
    }

    def __init__(self, assess=None, class_1=None, class_2=None):  # noqa: E501
        """CompatibilitiesSsdActiveItem - a model defined in Swagger"""  # noqa: E501

        self._assess = None
        self._class_1 = None
        self._class_2 = None
        self.discriminator = None

        if assess is not None:
            self.assess = assess
        self.class_1 = class_1
        if class_2 is not None:
            self.class_2 = class_2

    @property
    def assess(self):
        """Gets the assess of this CompatibilitiesSsdActiveItem.  # noqa: E501

        Do not create ssd compatibility, only assess if creation is possible.  # noqa: E501

        :return: The assess of this CompatibilitiesSsdActiveItem.  # noqa: E501
        :rtype: bool
        """
        return self._assess

    @assess.setter
    def assess(self, assess):
        """Sets the assess of this CompatibilitiesSsdActiveItem.

        Do not create ssd compatibility, only assess if creation is possible.  # noqa: E501

        :param assess: The assess of this CompatibilitiesSsdActiveItem.  # noqa: E501
        :type: bool
        """

        self._assess = assess

    @property
    def class_1(self):
        """Gets the class_1 of this CompatibilitiesSsdActiveItem.  # noqa: E501

        The node class of the desired ssd compatibility  # noqa: E501

        :return: The class_1 of this CompatibilitiesSsdActiveItem.  # noqa: E501
        :rtype: str
        """
        return self._class_1

    @class_1.setter
    def class_1(self, class_1):
        """Sets the class_1 of this CompatibilitiesSsdActiveItem.

        The node class of the desired ssd compatibility  # noqa: E501

        :param class_1: The class_1 of this CompatibilitiesSsdActiveItem.  # noqa: E501
        :type: str
        """
        if class_1 is None:
            raise ValueError("Invalid value for `class_1`, must not be `None`")  # noqa: E501

        self._class_1 = class_1

    @property
    def class_2(self):
        """Gets the class_2 of this CompatibilitiesSsdActiveItem.  # noqa: E501

        The optional second node class to turn on ssd compatibility  # noqa: E501

        :return: The class_2 of this CompatibilitiesSsdActiveItem.  # noqa: E501
        :rtype: str
        """
        return self._class_2

    @class_2.setter
    def class_2(self, class_2):
        """Sets the class_2 of this CompatibilitiesSsdActiveItem.

        The optional second node class to turn on ssd compatibility  # noqa: E501

        :param class_2: The class_2 of this CompatibilitiesSsdActiveItem.  # noqa: E501
        :type: str
        """

        self._class_2 = class_2

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
        if not isinstance(other, CompatibilitiesSsdActiveItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
