# V1beta1Policy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**created_at** | **datetime** | The time the policy was created. | [optional] 
**updated_at** | **datetime** | The time the policy was last updated. | [optional] 
**role_id** | **str** |  | [optional] 
**resource** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_policy import V1beta1Policy

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Policy from a JSON string
v1beta1_policy_instance = V1beta1Policy.from_json(json)
# print the JSON string representation of the object
print V1beta1Policy.to_json()

# convert the object into a dict
v1beta1_policy_dict = v1beta1_policy_instance.to_dict()
# create an instance of V1beta1Policy from a dict
v1beta1_policy_form_dict = v1beta1_policy.from_dict(v1beta1_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


