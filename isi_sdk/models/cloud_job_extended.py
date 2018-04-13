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

from isi_sdk_7_2.models.cloud_job_files import CloudJobFiles  # noqa: F401,E501
from isi_sdk_7_2.models.cloud_job_job_engine_job import CloudJobJobEngineJob  # noqa: F401,E501


class CloudJobExtended(object):
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
        'completion_time': 'int',
        'create_time': 'int',
        'description': 'str',
        'files': 'CloudJobFiles',
        'id': 'int',
        'job_engine_job': 'CloudJobJobEngineJob',
        'modified_time': 'int',
        'state': 'str',
        'type': 'str'
    }

    attribute_map = {
        'completion_time': 'completion_time',
        'create_time': 'create_time',
        'description': 'description',
        'files': 'files',
        'id': 'id',
        'job_engine_job': 'job_engine_job',
        'modified_time': 'modified_time',
        'state': 'state',
        'type': 'type'
    }

    def __init__(self, completion_time=None, create_time=None, description=None, files=None, id=None, job_engine_job=None, modified_time=None, state=None, type=None):  # noqa: E501
        """CloudJobExtended - a model defined in Swagger"""  # noqa: E501

        self._completion_time = None
        self._create_time = None
        self._description = None
        self._files = None
        self._id = None
        self._job_engine_job = None
        self._modified_time = None
        self._state = None
        self._type = None
        self.discriminator = None

        if completion_time is not None:
            self.completion_time = completion_time
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if files is not None:
            self.files = files
        if id is not None:
            self.id = id
        if job_engine_job is not None:
            self.job_engine_job = job_engine_job
        if modified_time is not None:
            self.modified_time = modified_time
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type

    @property
    def completion_time(self):
        """Gets the completion_time of this CloudJobExtended.  # noqa: E501

        The time at which the job was completed (if applicable)  # noqa: E501

        :return: The completion_time of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this CloudJobExtended.

        The time at which the job was completed (if applicable)  # noqa: E501

        :param completion_time: The completion_time of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._completion_time = completion_time

    @property
    def create_time(self):
        """Gets the create_time of this CloudJobExtended.  # noqa: E501

        The time at which the job was created  # noqa: E501

        :return: The create_time of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CloudJobExtended.

        The time at which the job was created  # noqa: E501

        :param create_time: The create_time of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this CloudJobExtended.  # noqa: E501

        A brief description of the job contents  # noqa: E501

        :return: The description of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudJobExtended.

        A brief description of the job contents  # noqa: E501

        :param description: The description of this CloudJobExtended.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def files(self):
        """Gets the files of this CloudJobExtended.  # noqa: E501

        The files and filters addressed by this job  # noqa: E501

        :return: The files of this CloudJobExtended.  # noqa: E501
        :rtype: CloudJobFiles
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this CloudJobExtended.

        The files and filters addressed by this job  # noqa: E501

        :param files: The files of this CloudJobExtended.  # noqa: E501
        :type: CloudJobFiles
        """

        self._files = files

    @property
    def id(self):
        """Gets the id of this CloudJobExtended.  # noqa: E501

        The job's ID  # noqa: E501

        :return: The id of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudJobExtended.

        The job's ID  # noqa: E501

        :param id: The id of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def job_engine_job(self):
        """Gets the job_engine_job of this CloudJobExtended.  # noqa: E501

        Information about the related job engine job if there is one  # noqa: E501

        :return: The job_engine_job of this CloudJobExtended.  # noqa: E501
        :rtype: CloudJobJobEngineJob
        """
        return self._job_engine_job

    @job_engine_job.setter
    def job_engine_job(self, job_engine_job):
        """Sets the job_engine_job of this CloudJobExtended.

        Information about the related job engine job if there is one  # noqa: E501

        :param job_engine_job: The job_engine_job of this CloudJobExtended.  # noqa: E501
        :type: CloudJobJobEngineJob
        """

        self._job_engine_job = job_engine_job

    @property
    def modified_time(self):
        """Gets the modified_time of this CloudJobExtended.  # noqa: E501

        The last time at which the job was modified  # noqa: E501

        :return: The modified_time of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this CloudJobExtended.

        The last time at which the job was modified  # noqa: E501

        :param modified_time: The modified_time of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._modified_time = modified_time

    @property
    def state(self):
        """Gets the state of this CloudJobExtended.  # noqa: E501

        The current state of the job  # noqa: E501

        :return: The state of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CloudJobExtended.

        The current state of the job  # noqa: E501

        :param state: The state of this CloudJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["running", "paused", "canceled", "completed", "failed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def type(self):
        """Gets the type of this CloudJobExtended.  # noqa: E501

        The type of cloud action to be performed by this job.  # noqa: E501

        :return: The type of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudJobExtended.

        The type of cloud action to be performed by this job.  # noqa: E501

        :param type: The type of this CloudJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["archive", "recall", "local-garbage-collection", "cloud-garbage-collection", "cache-writeback", "cache-on-access", "cache-invalidation"]  # noqa: E501
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
        if not isinstance(other, CloudJobExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
