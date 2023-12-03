# V1beta1Preference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**created_at** | **datetime** | The time when the preference was created. | [optional] 
**updated_at** | **datetime** | The time when the preference was updated. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_preference import V1beta1Preference

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Preference from a JSON string
v1beta1_preference_instance = V1beta1Preference.from_json(json)
# print the JSON string representation of the object
print V1beta1Preference.to_json()

# convert the object into a dict
v1beta1_preference_dict = v1beta1_preference_instance.to_dict()
# create an instance of V1beta1Preference from a dict
v1beta1_preference_form_dict = v1beta1_preference.from_dict(v1beta1_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


