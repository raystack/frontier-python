# V1beta1User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | Unique name of the user. | [optional] 
**title** | **str** | Name of the user. | [optional] 
**email** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** | The time the user was created. | [optional] 
**updated_at** | **datetime** | The time the user was last updated. | [optional] 
**state** | **str** | The state of the user (enabled or disabled). | [optional] 
**avatar** | **str** | The base64 encoded image string of the user avatar. Should be less than 2MB. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_user import V1beta1User

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1User from a JSON string
v1beta1_user_instance = V1beta1User.from_json(json)
# print the JSON string representation of the object
print V1beta1User.to_json()

# convert the object into a dict
v1beta1_user_dict = v1beta1_user_instance.to_dict()
# create an instance of V1beta1User from a dict
v1beta1_user_form_dict = v1beta1_user.from_dict(v1beta1_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


