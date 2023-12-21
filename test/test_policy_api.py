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

from frontier_api.api.policy_api import PolicyApi  # noqa: E501


class TestPolicyApi(unittest.TestCase):
    """PolicyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PolicyApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_frontier_service_create_policy(self) -> None:
        """Test case for frontier_service_create_policy

        Create policy  # noqa: E501
        """
        pass

    def test_frontier_service_delete_policy(self) -> None:
        """Test case for frontier_service_delete_policy

        Delete Policy  # noqa: E501
        """
        pass

    def test_frontier_service_get_policy(self) -> None:
        """Test case for frontier_service_get_policy

        Get policy  # noqa: E501
        """
        pass

    def test_frontier_service_list_policies(self) -> None:
        """Test case for frontier_service_list_policies

        List all policies  # noqa: E501
        """
        pass

    def test_frontier_service_update_policy(self) -> None:
        """Test case for frontier_service_update_policy

        Update policy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()