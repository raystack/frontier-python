# V1beta1SecretCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**secret** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** | The time when the secret was created. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_secret_credential import V1beta1SecretCredential

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1SecretCredential from a JSON string
v1beta1_secret_credential_instance = V1beta1SecretCredential.from_json(json)
# print the JSON string representation of the object
print V1beta1SecretCredential.to_json()

# convert the object into a dict
v1beta1_secret_credential_dict = v1beta1_secret_credential_instance.to_dict()
# create an instance of V1beta1SecretCredential from a dict
v1beta1_secret_credential_form_dict = v1beta1_secret_credential.from_dict(v1beta1_secret_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


