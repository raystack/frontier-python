# V1beta1Namespace


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** | The time the namespace was created. | [optional] 
**updated_at** | **datetime** | The time the namespace was last updated. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_namespace import V1beta1Namespace

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Namespace from a JSON string
v1beta1_namespace_instance = V1beta1Namespace.from_json(json)
# print the JSON string representation of the object
print V1beta1Namespace.to_json()

# convert the object into a dict
v1beta1_namespace_dict = v1beta1_namespace_instance.to_dict()
# create an instance of V1beta1Namespace from a dict
v1beta1_namespace_form_dict = v1beta1_namespace.from_dict(v1beta1_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


