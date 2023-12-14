# V1beta1GetServiceUserKeyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[V1beta1JSONWebKey]**](V1beta1JSONWebKey.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_service_user_key_response import V1beta1GetServiceUserKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetServiceUserKeyResponse from a JSON string
v1beta1_get_service_user_key_response_instance = V1beta1GetServiceUserKeyResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetServiceUserKeyResponse.to_json()

# convert the object into a dict
v1beta1_get_service_user_key_response_dict = v1beta1_get_service_user_key_response_instance.to_dict()
# create an instance of V1beta1GetServiceUserKeyResponse from a dict
v1beta1_get_service_user_key_response_form_dict = v1beta1_get_service_user_key_response.from_dict(v1beta1_get_service_user_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


