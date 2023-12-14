# V1beta1AddPlatformUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user id to add to the platform. | [optional] 
**serviceuser_id** | **str** | The service user id to add to the platform. | [optional] 
**relation** | **str** | The relation to add as in the platform. It can be admin or member. | 

## Example

```python
from frontier_api.models.v1beta1_add_platform_user_request import V1beta1AddPlatformUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AddPlatformUserRequest from a JSON string
v1beta1_add_platform_user_request_instance = V1beta1AddPlatformUserRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1AddPlatformUserRequest.to_json()

# convert the object into a dict
v1beta1_add_platform_user_request_dict = v1beta1_add_platform_user_request_instance.to_dict()
# create an instance of V1beta1AddPlatformUserRequest from a dict
v1beta1_add_platform_user_request_form_dict = v1beta1_add_platform_user_request.from_dict(v1beta1_add_platform_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


