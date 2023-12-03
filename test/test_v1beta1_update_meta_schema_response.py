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

from frontier_api.models.v1beta1_update_meta_schema_response import V1beta1UpdateMetaSchemaResponse

class TestV1beta1UpdateMetaSchemaResponse(unittest.TestCase):
    """V1beta1UpdateMetaSchemaResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1UpdateMetaSchemaResponse:
        """Test V1beta1UpdateMetaSchemaResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1UpdateMetaSchemaResponse`
        """
        model = V1beta1UpdateMetaSchemaResponse()
        if include_optional:
            return V1beta1UpdateMetaSchemaResponse(
                metaschema = frontier_api.models.v1beta1_meta_schema.v1beta1MetaSchema(
                    id = 'a9c4f4e2-9b9a-4c1a-8f1a-2b9b9b9b9b9b', 
                    name = '', 
                    schema = '', 
                    created_at = '2023-06-07T05:39:56.961Z', 
                    updated_at = '2023-06-07T05:39:56.961Z', )
            )
        else:
            return V1beta1UpdateMetaSchemaResponse(
        )
        """

    def testV1beta1UpdateMetaSchemaResponse(self):
        """Test V1beta1UpdateMetaSchemaResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
