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


class V1beta1PreferenceTrait(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            resourceType = schemas.StrSchema
            name = schemas.StrSchema
            title = schemas.StrSchema
            description = schemas.StrSchema
            longDescription = schemas.StrSchema
            heading = schemas.StrSchema
            subHeading = schemas.StrSchema
            breadcrumb = schemas.StrSchema
            inputHints = schemas.StrSchema
            text = schemas.StrSchema
            textarea = schemas.StrSchema
            select = schemas.StrSchema
            combobox = schemas.StrSchema
            checkbox = schemas.StrSchema
            multiselect = schemas.StrSchema
            number = schemas.StrSchema
            __annotations__ = {
                "resourceType": resourceType,
                "name": name,
                "title": title,
                "description": description,
                "longDescription": longDescription,
                "heading": heading,
                "subHeading": subHeading,
                "breadcrumb": breadcrumb,
                "inputHints": inputHints,
                "text": text,
                "textarea": textarea,
                "select": select,
                "combobox": combobox,
                "checkbox": checkbox,
                "multiselect": multiselect,
                "number": number,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longDescription"]) -> MetaOapg.properties.longDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heading"]) -> MetaOapg.properties.heading: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subHeading"]) -> MetaOapg.properties.subHeading: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breadcrumb"]) -> MetaOapg.properties.breadcrumb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputHints"]) -> MetaOapg.properties.inputHints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["textarea"]) -> MetaOapg.properties.textarea: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["select"]) -> MetaOapg.properties.select: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["combobox"]) -> MetaOapg.properties.combobox: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkbox"]) -> MetaOapg.properties.checkbox: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multiselect"]) -> MetaOapg.properties.multiselect: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resourceType", "name", "title", "description", "longDescription", "heading", "subHeading", "breadcrumb", "inputHints", "text", "textarea", "select", "combobox", "checkbox", "multiselect", "number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceType"]) -> typing.Union[MetaOapg.properties.resourceType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longDescription"]) -> typing.Union[MetaOapg.properties.longDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heading"]) -> typing.Union[MetaOapg.properties.heading, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subHeading"]) -> typing.Union[MetaOapg.properties.subHeading, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breadcrumb"]) -> typing.Union[MetaOapg.properties.breadcrumb, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputHints"]) -> typing.Union[MetaOapg.properties.inputHints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["textarea"]) -> typing.Union[MetaOapg.properties.textarea, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["select"]) -> typing.Union[MetaOapg.properties.select, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["combobox"]) -> typing.Union[MetaOapg.properties.combobox, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkbox"]) -> typing.Union[MetaOapg.properties.checkbox, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multiselect"]) -> typing.Union[MetaOapg.properties.multiselect, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resourceType", "name", "title", "description", "longDescription", "heading", "subHeading", "breadcrumb", "inputHints", "text", "textarea", "select", "combobox", "checkbox", "multiselect", "number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        resourceType: typing.Union[MetaOapg.properties.resourceType, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        longDescription: typing.Union[MetaOapg.properties.longDescription, str, schemas.Unset] = schemas.unset,
        heading: typing.Union[MetaOapg.properties.heading, str, schemas.Unset] = schemas.unset,
        subHeading: typing.Union[MetaOapg.properties.subHeading, str, schemas.Unset] = schemas.unset,
        breadcrumb: typing.Union[MetaOapg.properties.breadcrumb, str, schemas.Unset] = schemas.unset,
        inputHints: typing.Union[MetaOapg.properties.inputHints, str, schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        textarea: typing.Union[MetaOapg.properties.textarea, str, schemas.Unset] = schemas.unset,
        select: typing.Union[MetaOapg.properties.select, str, schemas.Unset] = schemas.unset,
        combobox: typing.Union[MetaOapg.properties.combobox, str, schemas.Unset] = schemas.unset,
        checkbox: typing.Union[MetaOapg.properties.checkbox, str, schemas.Unset] = schemas.unset,
        multiselect: typing.Union[MetaOapg.properties.multiselect, str, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1beta1PreferenceTrait':
        return super().__new__(
            cls,
            *_args,
            resourceType=resourceType,
            name=name,
            title=title,
            description=description,
            longDescription=longDescription,
            heading=heading,
            subHeading=subHeading,
            breadcrumb=breadcrumb,
            inputHints=inputHints,
            text=text,
            textarea=textarea,
            select=select,
            combobox=combobox,
            checkbox=checkbox,
            multiselect=multiselect,
            number=number,
            _configuration=_configuration,
            **kwargs,
        )
