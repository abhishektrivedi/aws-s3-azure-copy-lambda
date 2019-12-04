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

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from ..version import VERSION


class AzureBlobStorageConfiguration(Configuration):
    """Configuration for AzureBlobStorage
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param url: The URL of the service account, container, or blob that is the
     targe of the desired operation.
    :type url: str
    :ivar version: Specifies the version of the operation to use for this
     request.
    :type version: str
    """

    def __init__(self, url, **kwargs):

        if url is None:
            raise ValueError("Parameter 'url' must not be None.")

        super(AzureBlobStorageConfiguration, self).__init__(**kwargs)
        self._configure(**kwargs)

        self.user_agent_policy.add_user_agent('azsdk-python-azureblobstorage/{}'.format(VERSION))
        self.generate_client_request_id = True
        self.accept_language = None

        self.url = url
        self.version = "2019-02-02"

    def _configure(self, **kwargs):
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
