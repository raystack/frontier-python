# V1beta1MetaSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique metaschema uuid. | [optional] 
**name** | **str** |  | [optional] 
**var_schema** | **str** | The metaschema json schema. | [optional] 
**created_at** | **datetime** | The time when the metaschema was created. | [optional] 
**updated_at** | **datetime** | The time when the metaschema was updated. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_meta_schema import V1beta1MetaSchema

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1MetaSchema from a JSON string
v1beta1_meta_schema_instance = V1beta1MetaSchema.from_json(json)
# print the JSON string representation of the object
print V1beta1MetaSchema.to_json()

# convert the object into a dict
v1beta1_meta_schema_dict = v1beta1_meta_schema_instance.to_dict()
# create an instance of V1beta1MetaSchema from a dict
v1beta1_meta_schema_form_dict = v1beta1_meta_schema.from_dict(v1beta1_meta_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


