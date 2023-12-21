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

from frontier_api.api.relation_api import RelationApi  # noqa: E501


class TestRelationApi(unittest.TestCase):
    """RelationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RelationApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_admin_service_list_relations(self) -> None:
        """Test case for admin_service_list_relations

        List all relations  # noqa: E501
        """
        pass

    def test_frontier_service_create_relation(self) -> None:
        """Test case for frontier_service_create_relation

        Create relation  # noqa: E501
        """
        pass

    def test_frontier_service_delete_relation(self) -> None:
        """Test case for frontier_service_delete_relation

        Delete relation  # noqa: E501
        """
        pass

    def test_frontier_service_get_relation(self) -> None:
        """Test case for frontier_service_get_relation

        Get relation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()