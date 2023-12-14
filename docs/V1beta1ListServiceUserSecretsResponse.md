# V1beta1ListServiceUserSecretsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[V1beta1SecretCredential]**](V1beta1SecretCredential.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_service_user_secrets_response import V1beta1ListServiceUserSecretsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListServiceUserSecretsResponse from a JSON string
v1beta1_list_service_user_secrets_response_instance = V1beta1ListServiceUserSecretsResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListServiceUserSecretsResponse.to_json()

# convert the object into a dict
v1beta1_list_service_user_secrets_response_dict = v1beta1_list_service_user_secrets_response_instance.to_dict()
# create an instance of V1beta1ListServiceUserSecretsResponse from a dict
v1beta1_list_service_user_secrets_response_form_dict = v1beta1_list_service_user_secrets_response.from_dict(v1beta1_list_service_user_secrets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


