# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VSOnlinePlanProperties(Model):
    """VS Online Additional properties.

    Additional VS Online Plan properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param user_id: unique user assigned id.
    :type user_id: str
    :ivar service_uri: Service endpoint.
    :vartype service_uri: str
    """

    _validation = {
        'service_uri': {'readonly': True},
    }

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(self, *, user_id: str=None, **kwargs) -> None:
        super(VSOnlinePlanProperties, self).__init__(**kwargs)
        self.user_id = user_id
        self.service_uri = None
