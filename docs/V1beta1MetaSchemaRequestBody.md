# V1beta1MetaSchemaRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the metaschema. The name must be unique within the entire Frontier instance. The name can contain only alphanumeric characters, dashes and underscores. | 
**var_schema** | **str** | The schema of the metaschema. The schema must be a valid JSON schema.Please refer to https://json-schema.org/ to know more about json schema. | 

## Example

```python
from frontier_api.models.v1beta1_meta_schema_request_body import V1beta1MetaSchemaRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1MetaSchemaRequestBody from a JSON string
v1beta1_meta_schema_request_body_instance = V1beta1MetaSchemaRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1MetaSchemaRequestBody.to_json()

# convert the object into a dict
v1beta1_meta_schema_request_body_dict = v1beta1_meta_schema_request_body_instance.to_dict()
# create an instance of V1beta1MetaSchemaRequestBody from a dict
v1beta1_meta_schema_request_body_form_dict = v1beta1_meta_schema_request_body.from_dict(v1beta1_meta_schema_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


