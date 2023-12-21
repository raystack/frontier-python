# coding: utf-8

"""
    Frontier Administration API

    The Frontier APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Frontier APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Frontier APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Frontier into your existing applications and workflows.

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class V1beta1Role(BaseModel):
    """
    V1beta1Role
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    permissions: Optional[conlist(StrictStr)] = None
    title: Optional[StrictStr] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="The time the role was created.")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt", description="The time the role was last updated.")
    org_id: Optional[StrictStr] = Field(None, alias="orgId")
    state: Optional[StrictStr] = None
    scopes: Optional[conlist(StrictStr)] = None
    __properties = ["id", "name", "permissions", "title", "metadata", "createdAt", "updatedAt", "orgId", "state", "scopes"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1beta1Role:
        """Create an instance of V1beta1Role from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta1Role:
        """Create an instance of V1beta1Role from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta1Role.parse_obj(obj)

        _obj = V1beta1Role.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "permissions": obj.get("permissions"),
            "title": obj.get("title"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "org_id": obj.get("orgId"),
            "state": obj.get("state"),
            "scopes": obj.get("scopes")
        })
        return _obj

