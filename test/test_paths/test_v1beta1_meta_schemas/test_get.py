# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import shield_api
from shield_api.paths.v1beta1_meta_schemas import get  # noqa: E501
from shield_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1beta1MetaSchemas(ApiTestMixin, unittest.TestCase):
    """
    V1beta1MetaSchemas unit test stubs
        List metaschemas  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
