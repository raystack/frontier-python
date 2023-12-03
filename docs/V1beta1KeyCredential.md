# V1beta1KeyCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**principal_id** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] [readonly] 

## Example

```python
from frontier_api.models.v1beta1_key_credential import V1beta1KeyCredential

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1KeyCredential from a JSON string
v1beta1_key_credential_instance = V1beta1KeyCredential.from_json(json)
# print the JSON string representation of the object
print V1beta1KeyCredential.to_json()

# convert the object into a dict
v1beta1_key_credential_dict = v1beta1_key_credential_instance.to_dict()
# create an instance of V1beta1KeyCredential from a dict
v1beta1_key_credential_form_dict = v1beta1_key_credential.from_dict(v1beta1_key_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


