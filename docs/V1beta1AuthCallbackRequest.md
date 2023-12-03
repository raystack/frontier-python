# V1beta1AuthCallbackRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**state_options** | **object** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_auth_callback_request import V1beta1AuthCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AuthCallbackRequest from a JSON string
v1beta1_auth_callback_request_instance = V1beta1AuthCallbackRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1AuthCallbackRequest.to_json()

# convert the object into a dict
v1beta1_auth_callback_request_dict = v1beta1_auth_callback_request_instance.to_dict()
# create an instance of V1beta1AuthCallbackRequest from a dict
v1beta1_auth_callback_request_form_dict = v1beta1_auth_callback_request.from_dict(v1beta1_auth_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


