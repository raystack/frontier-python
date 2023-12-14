# V1beta1Permission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**created_at** | **datetime** | The time the permission was created. | [optional] 
**updated_at** | **datetime** | The time the permission was last updated. | [optional] 
**namespace** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**key** | **str** | Permission path key is composed of three parts, &#39;service.resource.verb&#39;. Where &#39;service.resource&#39; works as a namespace for the &#39;verb&#39;. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_permission import V1beta1Permission

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Permission from a JSON string
v1beta1_permission_instance = V1beta1Permission.from_json(json)
# print the JSON string representation of the object
print V1beta1Permission.to_json()

# convert the object into a dict
v1beta1_permission_dict = v1beta1_permission_instance.to_dict()
# create an instance of V1beta1Permission from a dict
v1beta1_permission_form_dict = v1beta1_permission.from_dict(v1beta1_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


