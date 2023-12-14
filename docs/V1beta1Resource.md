# V1beta1Resource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | Name of the resource. Must be unique within the project. | [optional] 
**created_at** | **datetime** | The time the resource was created. | [optional] 
**updated_at** | **datetime** | The time the resource was last updated. | [optional] 
**urn** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_resource import V1beta1Resource

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Resource from a JSON string
v1beta1_resource_instance = V1beta1Resource.from_json(json)
# print the JSON string representation of the object
print V1beta1Resource.to_json()

# convert the object into a dict
v1beta1_resource_dict = v1beta1_resource_instance.to_dict()
# create an instance of V1beta1Resource from a dict
v1beta1_resource_form_dict = v1beta1_resource.from_dict(v1beta1_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


