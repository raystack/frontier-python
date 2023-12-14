# V1beta1GetCurrentUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**V1beta1User**](V1beta1User.md) |  | [optional] 
**serviceuser** | [**V1beta1ServiceUser**](V1beta1ServiceUser.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_current_user_response import V1beta1GetCurrentUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetCurrentUserResponse from a JSON string
v1beta1_get_current_user_response_instance = V1beta1GetCurrentUserResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetCurrentUserResponse.to_json()

# convert the object into a dict
v1beta1_get_current_user_response_dict = v1beta1_get_current_user_response_instance.to_dict()
# create an instance of V1beta1GetCurrentUserResponse from a dict
v1beta1_get_current_user_response_form_dict = v1beta1_get_current_user_response.from_dict(v1beta1_get_current_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


