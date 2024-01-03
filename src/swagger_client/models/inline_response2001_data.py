# coding: utf-8

"""
    Khulnasoft API

    The official OpenAPI spec for the Khulnasoft API.  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse2001Data(object):
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
        "attributes": "InlineResponse2001DataAttributes",
        "links": "InlineResponse2001DataLinks",
        "id": "str",
        "type": "str",
    }

    attribute_map = {
        "attributes": "attributes",
        "links": "links",
        "id": "id",
        "type": "type",
    }

    def __init__(self, attributes=None, links=None, id=None, type=None):  # noqa: E501
        """InlineResponse2001Data - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._links = None
        self._id = None
        self._type = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse2001Data.  # noqa: E501


        :return: The attributes of this InlineResponse2001Data.  # noqa: E501
        :rtype: InlineResponse2001DataAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse2001Data.


        :param attributes: The attributes of this InlineResponse2001Data.  # noqa: E501
        :type: InlineResponse2001DataAttributes
        """

        self._attributes = attributes

    @property
    def links(self):
        """Gets the links of this InlineResponse2001Data.  # noqa: E501


        :return: The links of this InlineResponse2001Data.  # noqa: E501
        :rtype: InlineResponse2001DataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InlineResponse2001Data.


        :param links: The links of this InlineResponse2001Data.  # noqa: E501
        :type: InlineResponse2001DataLinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this InlineResponse2001Data.  # noqa: E501


        :return: The id of this InlineResponse2001Data.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2001Data.


        :param id: The id of this InlineResponse2001Data.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this InlineResponse2001Data.  # noqa: E501


        :return: The type of this InlineResponse2001Data.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2001Data.


        :param type: The type of this InlineResponse2001Data.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(InlineResponse2001Data, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
