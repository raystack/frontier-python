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

class V1beta1UserRequestBody(BaseModel):
    """
    V1beta1UserRequestBody
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the user. The name must be unique within the entire Frontier instance. The name can contain only alphanumeric characters, dashes and underscores and must start with a letter. If not provided, Frontier automatically generates a name from the user email. ")
    email: StrictStr = Field(description="The email of the user. The email must be unique within the entire Frontier instance.<br/>*Example:*`\"john.doe@raystack.org\"`")
    metadata: Optional[Union[str, Any]] = Field(default=None, description="Metadata object for users that can hold key value pairs pre-defined in User Metaschema. The metadata object can be used to store arbitrary information about the user such as label, description etc. By default the user metaschema contains labels and descriptions for the user. Update the same to add more fields to the user metadata object. <br/>*Example:*`{\"label\": {\"key1\": \"value1\"}, \"description\": \"User Description\"}`")
    title: Optional[StrictStr] = Field(default=None, description="The title can contain any UTF-8 character, used to provide a human-readable name for the user. Can also be left empty. <br/>*Example:*`\"John Doe\"`")
    avatar: Optional[StrictStr] = Field(default=None, description="The avatar is base64 encoded image data of the user. Can also be left empty. The image should be less than 200KB. Should follow the regex pattern `^data:image/(png|jpg|jpeg|gif);base64,([a-zA-Z0-9+/]+={0,2})+$`.")
    __properties: ClassVar[List[str]] = ["name", "email", "metadata", "title", "avatar"]

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
        """Create an instance of V1beta1UserRequestBody from a JSON string"""
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
        """Create an instance of V1beta1UserRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "metadata": obj.get("metadata"),
            "title": obj.get("title"),
            "avatar": obj.get("avatar")
        })
        return _obj


