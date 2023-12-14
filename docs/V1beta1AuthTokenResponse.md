# V1beta1AuthTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_auth_token_response import V1beta1AuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AuthTokenResponse from a JSON string
v1beta1_auth_token_response_instance = V1beta1AuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1AuthTokenResponse.to_json()

# convert the object into a dict
v1beta1_auth_token_response_dict = v1beta1_auth_token_response_instance.to_dict()
# create an instance of V1beta1AuthTokenResponse from a dict
v1beta1_auth_token_response_form_dict = v1beta1_auth_token_response.from_dict(v1beta1_auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


