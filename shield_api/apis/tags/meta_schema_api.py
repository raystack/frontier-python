# coding: utf-8

"""
    Shield Administration API

    The Shield APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Shield APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Shield APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Shield into your existing applications and workflows.  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by: https://openapi-generator.tech
"""

from shield_api.paths.v1beta1_meta_schemas.post import ShieldServiceCreateMetaSchema
from shield_api.paths.v1beta1_meta_schemas_id.delete import ShieldServiceDeleteMetaSchema
from shield_api.paths.v1beta1_meta_schemas_id.get import ShieldServiceGetMetaSchema
from shield_api.paths.v1beta1_meta_schemas.get import ShieldServiceListMetaSchemas
from shield_api.paths.v1beta1_meta_schemas_id.put import ShieldServiceUpdateMetaSchema


class MetaSchemaApi(
    ShieldServiceCreateMetaSchema,
    ShieldServiceDeleteMetaSchema,
    ShieldServiceGetMetaSchema,
    ShieldServiceListMetaSchemas,
    ShieldServiceUpdateMetaSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass