# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class NodesLnnStateNodeSmartfail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodesLnnStateNodeSmartfail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dead': 'bool',
            'down': 'bool',
            'in_cluster': 'bool',
            'readonly': 'bool',
            'shutdown_readonly': 'bool',
            'smartfailed': 'bool'
        }

        self.attribute_map = {
            'dead': 'dead',
            'down': 'down',
            'in_cluster': 'in_cluster',
            'readonly': 'readonly',
            'shutdown_readonly': 'shutdown_readonly',
            'smartfailed': 'smartfailed'
        }

        self._dead = None
        self._down = None
        self._in_cluster = None
        self._readonly = None
        self._shutdown_readonly = None
        self._smartfailed = None

    @property
    def dead(self):
        """
        Gets the dead of this NodesLnnStateNodeSmartfail.
        This node is dead (dead_devs).

        :return: The dead of this NodesLnnStateNodeSmartfail.
        :rtype: bool
        """
        return self._dead

    @dead.setter
    def dead(self, dead):
        """
        Sets the dead of this NodesLnnStateNodeSmartfail.
        This node is dead (dead_devs).

        :param dead: The dead of this NodesLnnStateNodeSmartfail.
        :type: bool
        """
        self._dead = dead

    @property
    def down(self):
        """
        Gets the down of this NodesLnnStateNodeSmartfail.
        This node is down (down_devs).

        :return: The down of this NodesLnnStateNodeSmartfail.
        :rtype: bool
        """
        return self._down

    @down.setter
    def down(self, down):
        """
        Sets the down of this NodesLnnStateNodeSmartfail.
        This node is down (down_devs).

        :param down: The down of this NodesLnnStateNodeSmartfail.
        :type: bool
        """
        self._down = down

    @property
    def in_cluster(self):
        """
        Gets the in_cluster of this NodesLnnStateNodeSmartfail.
        This node is in the cluster (all_devs).

        :return: The in_cluster of this NodesLnnStateNodeSmartfail.
        :rtype: bool
        """
        return self._in_cluster

    @in_cluster.setter
    def in_cluster(self, in_cluster):
        """
        Sets the in_cluster of this NodesLnnStateNodeSmartfail.
        This node is in the cluster (all_devs).

        :param in_cluster: The in_cluster of this NodesLnnStateNodeSmartfail.
        :type: bool
        """
        self._in_cluster = in_cluster

    @property
    def readonly(self):
        """
        Gets the readonly of this NodesLnnStateNodeSmartfail.
        This node is readonly (ro_devs).

        :return: The readonly of this NodesLnnStateNodeSmartfail.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """
        Sets the readonly of this NodesLnnStateNodeSmartfail.
        This node is readonly (ro_devs).

        :param readonly: The readonly of this NodesLnnStateNodeSmartfail.
        :type: bool
        """
        self._readonly = readonly

    @property
    def shutdown_readonly(self):
        """
        Gets the shutdown_readonly of this NodesLnnStateNodeSmartfail.
        This node is shutdown readonly (down_devs).

        :return: The shutdown_readonly of this NodesLnnStateNodeSmartfail.
        :rtype: bool
        """
        return self._shutdown_readonly

    @shutdown_readonly.setter
    def shutdown_readonly(self, shutdown_readonly):
        """
        Sets the shutdown_readonly of this NodesLnnStateNodeSmartfail.
        This node is shutdown readonly (down_devs).

        :param shutdown_readonly: The shutdown_readonly of this NodesLnnStateNodeSmartfail.
        :type: bool
        """
        self._shutdown_readonly = shutdown_readonly

    @property
    def smartfailed(self):
        """
        Gets the smartfailed of this NodesLnnStateNodeSmartfail.
        This node is smartfailed (soft_devs).

        :return: The smartfailed of this NodesLnnStateNodeSmartfail.
        :rtype: bool
        """
        return self._smartfailed

    @smartfailed.setter
    def smartfailed(self, smartfailed):
        """
        Sets the smartfailed of this NodesLnnStateNodeSmartfail.
        This node is smartfailed (soft_devs).

        :param smartfailed: The smartfailed of this NodesLnnStateNodeSmartfail.
        :type: bool
        """
        self._smartfailed = smartfailed

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
