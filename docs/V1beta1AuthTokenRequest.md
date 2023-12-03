# V1beta1AuthTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**assertion** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_auth_token_request import V1beta1AuthTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AuthTokenRequest from a JSON string
v1beta1_auth_token_request_instance = V1beta1AuthTokenRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1AuthTokenRequest.to_json()

# convert the object into a dict
v1beta1_auth_token_request_dict = v1beta1_auth_token_request_instance.to_dict()
# create an instance of V1beta1AuthTokenRequest from a dict
v1beta1_auth_token_request_form_dict = v1beta1_auth_token_request.from_dict(v1beta1_auth_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


