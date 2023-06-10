# coding: utf-8

# flake8: noqa

"""
    Shield Administration API

    The Shield APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Shield APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Shield APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Shield into your existing applications and workflows.  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by: https://openapi-generator.tech
"""

__version__ = "1.0.0"

# import ApiClient
from shield_api.api_client import ApiClient

# import Configuration
from shield_api.configuration import Configuration

# import exceptions
from shield_api.exceptions import OpenApiException
from shield_api.exceptions import ApiAttributeError
from shield_api.exceptions import ApiTypeError
from shield_api.exceptions import ApiValueError
from shield_api.exceptions import ApiKeyError
from shield_api.exceptions import ApiException