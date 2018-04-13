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

from isi_sdk_7_2.models.providers_krb5_id_params_keytab_entry import ProvidersKrb5IdParamsKeytabEntry  # noqa: F401,E501


class ProvidersKrb5Item(object):
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
        'keytab_entries': 'list[ProvidersKrb5IdParamsKeytabEntry]',
        'keytab_file': 'str',
        'manual_keying': 'bool',
        'name': 'str',
        'password': 'str',
        'realm': 'str',
        'user': 'str'
    }

    attribute_map = {
        'keytab_entries': 'keytab_entries',
        'keytab_file': 'keytab_file',
        'manual_keying': 'manual_keying',
        'name': 'name',
        'password': 'password',
        'realm': 'realm',
        'user': 'user'
    }

    def __init__(self, keytab_entries=None, keytab_file=None, manual_keying=None, name=None, password=None, realm=None, user=None):  # noqa: E501
        """ProvidersKrb5Item - a model defined in Swagger"""  # noqa: E501

        self._keytab_entries = None
        self._keytab_file = None
        self._manual_keying = None
        self._name = None
        self._password = None
        self._realm = None
        self._user = None
        self.discriminator = None

        if keytab_entries is not None:
            self.keytab_entries = keytab_entries
        if keytab_file is not None:
            self.keytab_file = keytab_file
        if manual_keying is not None:
            self.manual_keying = manual_keying
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        self.realm = realm
        if user is not None:
            self.user = user

    @property
    def keytab_entries(self):
        """Gets the keytab_entries of this ProvidersKrb5Item.  # noqa: E501

        Service principal names to register  # noqa: E501

        :return: The keytab_entries of this ProvidersKrb5Item.  # noqa: E501
        :rtype: list[ProvidersKrb5IdParamsKeytabEntry]
        """
        return self._keytab_entries

    @keytab_entries.setter
    def keytab_entries(self, keytab_entries):
        """Sets the keytab_entries of this ProvidersKrb5Item.

        Service principal names to register  # noqa: E501

        :param keytab_entries: The keytab_entries of this ProvidersKrb5Item.  # noqa: E501
        :type: list[ProvidersKrb5IdParamsKeytabEntry]
        """

        self._keytab_entries = keytab_entries

    @property
    def keytab_file(self):
        """Gets the keytab_file of this ProvidersKrb5Item.  # noqa: E501

        Path to a keytab file to import  # noqa: E501

        :return: The keytab_file of this ProvidersKrb5Item.  # noqa: E501
        :rtype: str
        """
        return self._keytab_file

    @keytab_file.setter
    def keytab_file(self, keytab_file):
        """Sets the keytab_file of this ProvidersKrb5Item.

        Path to a keytab file to import  # noqa: E501

        :param keytab_file: The keytab_file of this ProvidersKrb5Item.  # noqa: E501
        :type: str
        """

        self._keytab_file = keytab_file

    @property
    def manual_keying(self):
        """Gets the manual_keying of this ProvidersKrb5Item.  # noqa: E501

        Indicates keys are managed manually rather than with kadmin  # noqa: E501

        :return: The manual_keying of this ProvidersKrb5Item.  # noqa: E501
        :rtype: bool
        """
        return self._manual_keying

    @manual_keying.setter
    def manual_keying(self, manual_keying):
        """Sets the manual_keying of this ProvidersKrb5Item.

        Indicates keys are managed manually rather than with kadmin  # noqa: E501

        :param manual_keying: The manual_keying of this ProvidersKrb5Item.  # noqa: E501
        :type: bool
        """

        self._manual_keying = manual_keying

    @property
    def name(self):
        """Gets the name of this ProvidersKrb5Item.  # noqa: E501

        Specifies Kerberos provider name.  # noqa: E501

        :return: The name of this ProvidersKrb5Item.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvidersKrb5Item.

        Specifies Kerberos provider name.  # noqa: E501

        :param name: The name of this ProvidersKrb5Item.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """Gets the password of this ProvidersKrb5Item.  # noqa: E501


        :return: The password of this ProvidersKrb5Item.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ProvidersKrb5Item.


        :param password: The password of this ProvidersKrb5Item.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def realm(self):
        """Gets the realm of this ProvidersKrb5Item.  # noqa: E501

        Name of realm we are joined to  # noqa: E501

        :return: The realm of this ProvidersKrb5Item.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this ProvidersKrb5Item.

        Name of realm we are joined to  # noqa: E501

        :param realm: The realm of this ProvidersKrb5Item.  # noqa: E501
        :type: str
        """
        if realm is None:
            raise ValueError("Invalid value for `realm`, must not be `None`")  # noqa: E501

        self._realm = realm

    @property
    def user(self):
        """Gets the user of this ProvidersKrb5Item.  # noqa: E501

        Name of the user to use for kadmin tasks  # noqa: E501

        :return: The user of this ProvidersKrb5Item.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ProvidersKrb5Item.

        Name of the user to use for kadmin tasks  # noqa: E501

        :param user: The user of this ProvidersKrb5Item.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if not isinstance(other, ProvidersKrb5Item):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
