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
import datetime

from frontier_api.models.v1beta1_list_organization_audit_logs_response import V1beta1ListOrganizationAuditLogsResponse  # noqa: E501

class TestV1beta1ListOrganizationAuditLogsResponse(unittest.TestCase):
    """V1beta1ListOrganizationAuditLogsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1ListOrganizationAuditLogsResponse:
        """Test V1beta1ListOrganizationAuditLogsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1ListOrganizationAuditLogsResponse`
        """
        model = V1beta1ListOrganizationAuditLogsResponse()  # noqa: E501
        if include_optional:
            return V1beta1ListOrganizationAuditLogsResponse(
                logs = [
                    frontier_api.models.v1beta1_audit_log.v1beta1AuditLog(
                        id = '', 
                        source = 'auth', 
                        action = '', 
                        actor = frontier_api.models.v1beta1_audit_log_actor.v1beta1AuditLogActor(
                            id = '', 
                            type = '', 
                            name = '', ), 
                        target = frontier_api.models.v1beta1_audit_log_target.v1beta1AuditLogTarget(
                            id = '', 
                            type = '', 
                            name = '', ), 
                        context = {
                            'key' : ''
                            }, 
                        created_at = '2023-06-07T05:39:56.961Z', )
                    ]
            )
        else:
            return V1beta1ListOrganizationAuditLogsResponse(
        )
        """

    def testV1beta1ListOrganizationAuditLogsResponse(self):
        """Test V1beta1ListOrganizationAuditLogsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
