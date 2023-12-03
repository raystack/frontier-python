# V1beta1GetMetaSchemaResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metaschema** | [**V1beta1MetaSchema**](V1beta1MetaSchema.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_meta_schema_response import V1beta1GetMetaSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetMetaSchemaResponse from a JSON string
v1beta1_get_meta_schema_response_instance = V1beta1GetMetaSchemaResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetMetaSchemaResponse.to_json()

# convert the object into a dict
v1beta1_get_meta_schema_response_dict = v1beta1_get_meta_schema_response_instance.to_dict()
# create an instance of V1beta1GetMetaSchemaResponse from a dict
v1beta1_get_meta_schema_response_form_dict = v1beta1_get_meta_schema_response.from_dict(v1beta1_get_meta_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


