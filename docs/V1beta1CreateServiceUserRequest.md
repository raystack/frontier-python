# V1beta1CreateServiceUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**V1beta1ServiceUserRequestBody**](V1beta1ServiceUserRequestBody.md) |  | [optional] 
**org_id** | **str** | The organization ID to which the service user belongs to. | 

## Example

```python
from frontier_api.models.v1beta1_create_service_user_request import V1beta1CreateServiceUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CreateServiceUserRequest from a JSON string
v1beta1_create_service_user_request_instance = V1beta1CreateServiceUserRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1CreateServiceUserRequest.to_json()

# convert the object into a dict
v1beta1_create_service_user_request_dict = v1beta1_create_service_user_request_instance.to_dict()
# create an instance of V1beta1CreateServiceUserRequest from a dict
v1beta1_create_service_user_request_form_dict = v1beta1_create_service_user_request.from_dict(v1beta1_create_service_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


