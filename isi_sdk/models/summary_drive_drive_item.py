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


class SummaryDriveDriveItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SummaryDriveDriveItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_latency': 'float',
            'access_slow': 'float',
            'busy': 'float',
            'bytes_in': 'float',
            'bytes_out': 'float',
            'drive_id': 'str',
            'iosched_latency': 'float',
            'iosched_queue': 'float',
            'time': 'int',
            'type': 'str',
            'used_bytes_percent': 'float',
            'used_inodes': 'float',
            'xfer_size_in': 'float',
            'xfer_size_out': 'float',
            'xfers_in': 'float',
            'xfers_out': 'float'
        }

        self.attribute_map = {
            'access_latency': 'access_latency',
            'access_slow': 'access_slow',
            'busy': 'busy',
            'bytes_in': 'bytes_in',
            'bytes_out': 'bytes_out',
            'drive_id': 'drive_id',
            'iosched_latency': 'iosched_latency',
            'iosched_queue': 'iosched_queue',
            'time': 'time',
            'type': 'type',
            'used_bytes_percent': 'used_bytes_percent',
            'used_inodes': 'used_inodes',
            'xfer_size_in': 'xfer_size_in',
            'xfer_size_out': 'xfer_size_out',
            'xfers_in': 'xfers_in',
            'xfers_out': 'xfers_out'
        }

        self._access_latency = None
        self._access_slow = None
        self._busy = None
        self._bytes_in = None
        self._bytes_out = None
        self._drive_id = None
        self._iosched_latency = None
        self._iosched_queue = None
        self._time = None
        self._type = None
        self._used_bytes_percent = None
        self._used_inodes = None
        self._xfer_size_in = None
        self._xfer_size_out = None
        self._xfers_in = None
        self._xfers_out = None

    @property
    def access_latency(self):
        """
        Gets the access_latency of this SummaryDriveDriveItem.
        The average operation latency.

        :return: The access_latency of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._access_latency

    @access_latency.setter
    def access_latency(self, access_latency):
        """
        Sets the access_latency of this SummaryDriveDriveItem.
        The average operation latency.

        :param access_latency: The access_latency of this SummaryDriveDriveItem.
        :type: float
        """
        self._access_latency = access_latency

    @property
    def access_slow(self):
        """
        Gets the access_slow of this SummaryDriveDriveItem.
        The rate of slow (long-latency) operations.

        :return: The access_slow of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._access_slow

    @access_slow.setter
    def access_slow(self, access_slow):
        """
        Sets the access_slow of this SummaryDriveDriveItem.
        The rate of slow (long-latency) operations.

        :param access_slow: The access_slow of this SummaryDriveDriveItem.
        :type: float
        """
        self._access_slow = access_slow

    @property
    def busy(self):
        """
        Gets the busy of this SummaryDriveDriveItem.
        The percentage of time the drive was busy.

        :return: The busy of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._busy

    @busy.setter
    def busy(self, busy):
        """
        Sets the busy of this SummaryDriveDriveItem.
        The percentage of time the drive was busy.

        :param busy: The busy of this SummaryDriveDriveItem.
        :type: float
        """
        self._busy = busy

    @property
    def bytes_in(self):
        """
        Gets the bytes_in of this SummaryDriveDriveItem.
        The rate of bytes written.

        :return: The bytes_in of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._bytes_in

    @bytes_in.setter
    def bytes_in(self, bytes_in):
        """
        Sets the bytes_in of this SummaryDriveDriveItem.
        The rate of bytes written.

        :param bytes_in: The bytes_in of this SummaryDriveDriveItem.
        :type: float
        """
        self._bytes_in = bytes_in

    @property
    def bytes_out(self):
        """
        Gets the bytes_out of this SummaryDriveDriveItem.
        The rate of bytes read.

        :return: The bytes_out of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._bytes_out

    @bytes_out.setter
    def bytes_out(self, bytes_out):
        """
        Sets the bytes_out of this SummaryDriveDriveItem.
        The rate of bytes read.

        :param bytes_out: The bytes_out of this SummaryDriveDriveItem.
        :type: float
        """
        self._bytes_out = bytes_out

    @property
    def drive_id(self):
        """
        Gets the drive_id of this SummaryDriveDriveItem.
        Drive ID LNN:bay.

        :return: The drive_id of this SummaryDriveDriveItem.
        :rtype: str
        """
        return self._drive_id

    @drive_id.setter
    def drive_id(self, drive_id):
        """
        Sets the drive_id of this SummaryDriveDriveItem.
        Drive ID LNN:bay.

        :param drive_id: The drive_id of this SummaryDriveDriveItem.
        :type: str
        """
        self._drive_id = drive_id

    @property
    def iosched_latency(self):
        """
        Gets the iosched_latency of this SummaryDriveDriveItem.
        The average time spent in the I/O scheduler.

        :return: The iosched_latency of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._iosched_latency

    @iosched_latency.setter
    def iosched_latency(self, iosched_latency):
        """
        Sets the iosched_latency of this SummaryDriveDriveItem.
        The average time spent in the I/O scheduler.

        :param iosched_latency: The iosched_latency of this SummaryDriveDriveItem.
        :type: float
        """
        self._iosched_latency = iosched_latency

    @property
    def iosched_queue(self):
        """
        Gets the iosched_queue of this SummaryDriveDriveItem.
        The average length of the I/O scheduler queue.

        :return: The iosched_queue of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._iosched_queue

    @iosched_queue.setter
    def iosched_queue(self, iosched_queue):
        """
        Sets the iosched_queue of this SummaryDriveDriveItem.
        The average length of the I/O scheduler queue.

        :param iosched_queue: The iosched_queue of this SummaryDriveDriveItem.
        :type: float
        """
        self._iosched_queue = iosched_queue

    @property
    def time(self):
        """
        Gets the time of this SummaryDriveDriveItem.
        Unix Epoch time in seconds of the request.

        :return: The time of this SummaryDriveDriveItem.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this SummaryDriveDriveItem.
        Unix Epoch time in seconds of the request.

        :param time: The time of this SummaryDriveDriveItem.
        :type: int
        """
        self._time = time

    @property
    def type(self):
        """
        Gets the type of this SummaryDriveDriveItem.
        The type of the drive.

        :return: The type of this SummaryDriveDriveItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SummaryDriveDriveItem.
        The type of the drive.

        :param type: The type of this SummaryDriveDriveItem.
        :type: str
        """
        self._type = type

    @property
    def used_bytes_percent(self):
        """
        Gets the used_bytes_percent of this SummaryDriveDriveItem.
        The percent of blocks used on the drive.

        :return: The used_bytes_percent of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._used_bytes_percent

    @used_bytes_percent.setter
    def used_bytes_percent(self, used_bytes_percent):
        """
        Sets the used_bytes_percent of this SummaryDriveDriveItem.
        The percent of blocks used on the drive.

        :param used_bytes_percent: The used_bytes_percent of this SummaryDriveDriveItem.
        :type: float
        """
        self._used_bytes_percent = used_bytes_percent

    @property
    def used_inodes(self):
        """
        Gets the used_inodes of this SummaryDriveDriveItem.
        The number of inodes allocated on the drive.

        :return: The used_inodes of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._used_inodes

    @used_inodes.setter
    def used_inodes(self, used_inodes):
        """
        Sets the used_inodes of this SummaryDriveDriveItem.
        The number of inodes allocated on the drive.

        :param used_inodes: The used_inodes of this SummaryDriveDriveItem.
        :type: float
        """
        self._used_inodes = used_inodes

    @property
    def xfer_size_in(self):
        """
        Gets the xfer_size_in of this SummaryDriveDriveItem.
        The average size of write operations.

        :return: The xfer_size_in of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._xfer_size_in

    @xfer_size_in.setter
    def xfer_size_in(self, xfer_size_in):
        """
        Sets the xfer_size_in of this SummaryDriveDriveItem.
        The average size of write operations.

        :param xfer_size_in: The xfer_size_in of this SummaryDriveDriveItem.
        :type: float
        """
        self._xfer_size_in = xfer_size_in

    @property
    def xfer_size_out(self):
        """
        Gets the xfer_size_out of this SummaryDriveDriveItem.
        The average size of read operations.

        :return: The xfer_size_out of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._xfer_size_out

    @xfer_size_out.setter
    def xfer_size_out(self, xfer_size_out):
        """
        Sets the xfer_size_out of this SummaryDriveDriveItem.
        The average size of read operations.

        :param xfer_size_out: The xfer_size_out of this SummaryDriveDriveItem.
        :type: float
        """
        self._xfer_size_out = xfer_size_out

    @property
    def xfers_in(self):
        """
        Gets the xfers_in of this SummaryDriveDriveItem.
        The rate of write operations.

        :return: The xfers_in of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._xfers_in

    @xfers_in.setter
    def xfers_in(self, xfers_in):
        """
        Sets the xfers_in of this SummaryDriveDriveItem.
        The rate of write operations.

        :param xfers_in: The xfers_in of this SummaryDriveDriveItem.
        :type: float
        """
        self._xfers_in = xfers_in

    @property
    def xfers_out(self):
        """
        Gets the xfers_out of this SummaryDriveDriveItem.
        The rate of read operations.

        :return: The xfers_out of this SummaryDriveDriveItem.
        :rtype: float
        """
        return self._xfers_out

    @xfers_out.setter
    def xfers_out(self, xfers_out):
        """
        Sets the xfers_out of this SummaryDriveDriveItem.
        The rate of read operations.

        :param xfers_out: The xfers_out of this SummaryDriveDriveItem.
        :type: float
        """
        self._xfers_out = xfers_out

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
