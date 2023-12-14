# V1beta1ServiceUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** | User friendly name of the service user. | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** | The time the user was created. | [optional] 
**updated_at** | **datetime** | The time the user was last updated. | [optional] 
**state** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_service_user import V1beta1ServiceUser

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ServiceUser from a JSON string
v1beta1_service_user_instance = V1beta1ServiceUser.from_json(json)
# print the JSON string representation of the object
print V1beta1ServiceUser.to_json()

# convert the object into a dict
v1beta1_service_user_dict = v1beta1_service_user_instance.to_dict()
# create an instance of V1beta1ServiceUser from a dict
v1beta1_service_user_form_dict = v1beta1_service_user.from_dict(v1beta1_service_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


