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

from frontier_api.api.billing_api import BillingApi


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BillingApi()

    def tearDown(self) -> None:
        pass

    def test_frontier_service_create_billing_account(self) -> None:
        """Test case for frontier_service_create_billing_account

        Create billing account
        """
        pass

    def test_frontier_service_delete_billing_account(self) -> None:
        """Test case for frontier_service_delete_billing_account

        Delete billing account
        """
        pass

    def test_frontier_service_get_billing_account(self) -> None:
        """Test case for frontier_service_get_billing_account

        Get billing account
        """
        pass

    def test_frontier_service_get_billing_balance(self) -> None:
        """Test case for frontier_service_get_billing_balance

        Get billing balance
        """
        pass

    def test_frontier_service_list_billing_accounts(self) -> None:
        """Test case for frontier_service_list_billing_accounts

        List billing accounts
        """
        pass

    def test_frontier_service_update_billing_account(self) -> None:
        """Test case for frontier_service_update_billing_account

        Update billing account
        """
        pass


if __name__ == '__main__':
    unittest.main()
