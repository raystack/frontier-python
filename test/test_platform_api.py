# coding: utf-8

"""
    Frontier Administration API

    The Frontier APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Frontier APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Frontier APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Frontier into your existing applications and workflows.

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from frontier_api.api.platform_api import PlatformApi  # noqa: E501


class TestPlatformApi(unittest.TestCase):
    """PlatformApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlatformApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_admin_service_add_platform_user(self) -> None:
        """Test case for admin_service_add_platform_user

        Add platform user  # noqa: E501
        """
        pass

    def test_admin_service_list_platform_users(self) -> None:
        """Test case for admin_service_list_platform_users

        List platform users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
