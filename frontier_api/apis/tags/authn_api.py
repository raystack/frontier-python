# coding: utf-8

"""
    Frontier Administration API

    The Frontier APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Frontier APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Frontier APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Frontier into your existing applications and workflows.  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by: https://openapi-generator.tech
"""

from frontier_api.paths.v1beta1_auth_callback.get import FrontierServiceAuthCallback
from frontier_api.paths.v1beta1_auth_callback.post import FrontierServiceAuthCallback2
from frontier_api.paths.v1beta1_auth_logout.get import FrontierServiceAuthLogout
from frontier_api.paths.v1beta1_auth_logout.delete import FrontierServiceAuthLogout2
from frontier_api.paths.v1beta1_auth_token.post import FrontierServiceAuthToken
from frontier_api.paths.v1beta1_auth_register_strategy_name.get import FrontierServiceAuthenticate
from frontier_api.paths.v1beta1_auth_register_strategy_name.post import FrontierServiceAuthenticate2
from frontier_api.paths.v1beta1_auth.get import FrontierServiceListAuthStrategies


class AuthnApi(
    FrontierServiceAuthCallback,
    FrontierServiceAuthCallback2,
    FrontierServiceAuthLogout,
    FrontierServiceAuthLogout2,
    FrontierServiceAuthToken,
    FrontierServiceAuthenticate,
    FrontierServiceAuthenticate2,
    FrontierServiceListAuthStrategies,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass