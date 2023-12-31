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

from frontier_api.api.organization_api import OrganizationApi  # noqa: E501


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_admin_service_list_all_organizations(self) -> None:
        """Test case for admin_service_list_all_organizations

        List all organizations  # noqa: E501
        """
        pass

    def test_frontier_service_accept_organization_invitation(self) -> None:
        """Test case for frontier_service_accept_organization_invitation

        Accept pending invitation  # noqa: E501
        """
        pass

    def test_frontier_service_add_organization_users(self) -> None:
        """Test case for frontier_service_add_organization_users

        Add organization user  # noqa: E501
        """
        pass

    def test_frontier_service_create_organization(self) -> None:
        """Test case for frontier_service_create_organization

        Create organization  # noqa: E501
        """
        pass

    def test_frontier_service_create_organization_domain(self) -> None:
        """Test case for frontier_service_create_organization_domain

        Create org domain  # noqa: E501
        """
        pass

    def test_frontier_service_create_organization_invitation(self) -> None:
        """Test case for frontier_service_create_organization_invitation

        Invite user  # noqa: E501
        """
        pass

    def test_frontier_service_delete_organization(self) -> None:
        """Test case for frontier_service_delete_organization

        Delete organization  # noqa: E501
        """
        pass

    def test_frontier_service_delete_organization_domain(self) -> None:
        """Test case for frontier_service_delete_organization_domain

        Delete org domain  # noqa: E501
        """
        pass

    def test_frontier_service_delete_organization_invitation(self) -> None:
        """Test case for frontier_service_delete_organization_invitation

        Delete pending invitation  # noqa: E501
        """
        pass

    def test_frontier_service_disable_organization(self) -> None:
        """Test case for frontier_service_disable_organization

        Disable organization  # noqa: E501
        """
        pass

    def test_frontier_service_enable_organization(self) -> None:
        """Test case for frontier_service_enable_organization

        Enable organization  # noqa: E501
        """
        pass

    def test_frontier_service_get_organization(self) -> None:
        """Test case for frontier_service_get_organization

        Get organization  # noqa: E501
        """
        pass

    def test_frontier_service_get_organization_domain(self) -> None:
        """Test case for frontier_service_get_organization_domain

        Get org domain  # noqa: E501
        """
        pass

    def test_frontier_service_get_organization_invitation(self) -> None:
        """Test case for frontier_service_get_organization_invitation

        Get pending invitation  # noqa: E501
        """
        pass

    def test_frontier_service_join_organization(self) -> None:
        """Test case for frontier_service_join_organization

        Join organization  # noqa: E501
        """
        pass

    def test_frontier_service_list_organization_admins(self) -> None:
        """Test case for frontier_service_list_organization_admins

        List organization admins  # noqa: E501
        """
        pass

    def test_frontier_service_list_organization_domains(self) -> None:
        """Test case for frontier_service_list_organization_domains

        List org domains  # noqa: E501
        """
        pass

    def test_frontier_service_list_organization_invitations(self) -> None:
        """Test case for frontier_service_list_organization_invitations

        List pending invitations  # noqa: E501
        """
        pass

    def test_frontier_service_list_organization_projects(self) -> None:
        """Test case for frontier_service_list_organization_projects

        Get organization projects  # noqa: E501
        """
        pass

    def test_frontier_service_list_organization_service_users(self) -> None:
        """Test case for frontier_service_list_organization_service_users

        List organization service users  # noqa: E501
        """
        pass

    def test_frontier_service_list_organization_users(self) -> None:
        """Test case for frontier_service_list_organization_users

        List organization users  # noqa: E501
        """
        pass

    def test_frontier_service_list_organizations(self) -> None:
        """Test case for frontier_service_list_organizations

        List organizations  # noqa: E501
        """
        pass

    def test_frontier_service_remove_organization_user(self) -> None:
        """Test case for frontier_service_remove_organization_user

        Remove organization user  # noqa: E501
        """
        pass

    def test_frontier_service_update_organization(self) -> None:
        """Test case for frontier_service_update_organization

        Update organization  # noqa: E501
        """
        pass

    def test_frontier_service_verify_organization_domain(self) -> None:
        """Test case for frontier_service_verify_organization_domain

        Verify org domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
