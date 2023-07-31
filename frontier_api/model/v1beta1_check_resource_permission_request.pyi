# coding: utf-8

"""
    Frontier Administration API

    The Frontier APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Frontier APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Frontier APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Frontier into your existing applications and workflows.  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from frontier_api import schemas  # noqa: F401


class V1beta1CheckResourcePermissionRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "permission",
        }
        
        class properties:
            permission = schemas.StrSchema
            objectId = schemas.StrSchema
            objectNamespace = schemas.StrSchema
            resource = schemas.StrSchema
            __annotations__ = {
                "permission": permission,
                "objectId": objectId,
                "objectNamespace": objectNamespace,
                "resource": resource,
            }
    
    permission: MetaOapg.properties.permission
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permission"]) -> MetaOapg.properties.permission: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectId"]) -> MetaOapg.properties.objectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectNamespace"]) -> MetaOapg.properties.objectNamespace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> MetaOapg.properties.resource: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["permission", "objectId", "objectNamespace", "resource", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permission"]) -> MetaOapg.properties.permission: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectId"]) -> typing.Union[MetaOapg.properties.objectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectNamespace"]) -> typing.Union[MetaOapg.properties.objectNamespace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> typing.Union[MetaOapg.properties.resource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["permission", "objectId", "objectNamespace", "resource", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        permission: typing.Union[MetaOapg.properties.permission, str, ],
        objectId: typing.Union[MetaOapg.properties.objectId, str, schemas.Unset] = schemas.unset,
        objectNamespace: typing.Union[MetaOapg.properties.objectNamespace, str, schemas.Unset] = schemas.unset,
        resource: typing.Union[MetaOapg.properties.resource, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1beta1CheckResourcePermissionRequest':
        return super().__new__(
            cls,
            *_args,
            permission=permission,
            objectId=objectId,
            objectNamespace=objectNamespace,
            resource=resource,
            _configuration=_configuration,
            **kwargs,
        )