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

from frontier_api.models.v1beta1_billing_account_request_body import V1beta1BillingAccountRequestBody  # noqa: E501

class TestV1beta1BillingAccountRequestBody(unittest.TestCase):
    """V1beta1BillingAccountRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1BillingAccountRequestBody:
        """Test V1beta1BillingAccountRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1BillingAccountRequestBody`
        """
        model = V1beta1BillingAccountRequestBody()  # noqa: E501
        if include_optional:
            return V1beta1BillingAccountRequestBody(
                name = '',
                email = '',
                phone = '',
                address = frontier_api.models.billing_account_address.BillingAccountAddress(
                    line1 = '', 
                    line2 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country = '', ),
                currency = '',
                metadata = None
            )
        else:
            return V1beta1BillingAccountRequestBody(
        )
        """

    def testV1beta1BillingAccountRequestBody(self):
        """Test V1beta1BillingAccountRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()