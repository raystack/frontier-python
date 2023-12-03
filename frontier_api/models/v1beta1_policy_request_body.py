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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1beta1PolicyRequestBody(BaseModel):
    """
    V1beta1PolicyRequestBody
    """ # noqa: E501
    role_id: StrictStr = Field(description="unique id of the role to which policy is assigned", alias="roleId")
    title: Optional[StrictStr] = Field(default=None, description="The title can contain any UTF-8 character, used to provide a human-readable name for the policy. Can also be left empty. <br/> *Example:* `Policy title`")
    resource: StrictStr = Field(description="The resource to which policy is assigned in this format `namespace:uuid`. <br/> *Example:* `app/guardian:70f69c3a-334b-4f25-90b8-4d4f3be6b8e2`")
    principal: StrictStr = Field(description="principal is the user or group to which policy is assigned. The principal id must be prefixed with its namespace id in this format `namespace:uuid`. The namespace can be `app/user`, `app/group` or `app/serviceuser` (coming up!) and uuid is the unique id of the principal. <br/> *Example:* `app/user:92f69c3a-334b-4f25-90b8-4d4f3be6b825`")
    metadata: Optional[Union[str, Any]] = Field(default=None, description="Metadata object for policies that can hold key value pairs defined in Policy Metaschema.<br/> *Example:* `{\"labels\": {\"key\": \"value\"}, \"description\": \"Policy description\"}`")
    __properties: ClassVar[List[str]] = ["roleId", "title", "resource", "principal", "metadata"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V1beta1PolicyRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1beta1PolicyRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "roleId": obj.get("roleId"),
            "title": obj.get("title"),
            "resource": obj.get("resource"),
            "principal": obj.get("principal"),
            "metadata": obj.get("metadata")
        })
        return _obj


