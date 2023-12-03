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

from frontier_api.models.v1beta1_update_current_user_response import V1beta1UpdateCurrentUserResponse

class TestV1beta1UpdateCurrentUserResponse(unittest.TestCase):
    """V1beta1UpdateCurrentUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1UpdateCurrentUserResponse:
        """Test V1beta1UpdateCurrentUserResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1UpdateCurrentUserResponse`
        """
        model = V1beta1UpdateCurrentUserResponse()
        if include_optional:
            return V1beta1UpdateCurrentUserResponse(
                user = frontier_api.models.v1beta1_user.v1beta1User(
                    id = '', 
                    name = 'johndoe', 
                    title = 'John Doe', 
                    email = '', 
                    metadata = frontier_api.models.metadata.metadata(), 
                    created_at = '2023-06-07T05:39:56.961Z', 
                    updated_at = '2023-06-07T05:39:56.961Z', 
                    state = 'enabled', 
                    avatar = '', )
            )
        else:
            return V1beta1UpdateCurrentUserResponse(
        )
        """

    def testV1beta1UpdateCurrentUserResponse(self):
        """Test V1beta1UpdateCurrentUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
