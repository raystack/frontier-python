# V1beta1JSONWebKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Key Type. | [optional] 
**alg** | **str** | Algorithm. | [optional] 
**use** | **str** | Permitted uses for the public keys. | [optional] 
**kid** | **str** | Key ID. | [optional] 
**n** | **str** | Used for RSA keys. | [optional] 
**e** | **str** | Used for RSA keys. | [optional] 
**x** | **str** | Used for ECDSA keys. | [optional] 
**y** | **str** | Used for ECDSA keys. | [optional] 
**crv** | **str** | Used for ECDSA keys. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_json_web_key import V1beta1JSONWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1JSONWebKey from a JSON string
v1beta1_json_web_key_instance = V1beta1JSONWebKey.from_json(json)
# print the JSON string representation of the object
print V1beta1JSONWebKey.to_json()

# convert the object into a dict
v1beta1_json_web_key_dict = v1beta1_json_web_key_instance.to_dict()
# create an instance of V1beta1JSONWebKey from a dict
v1beta1_json_web_key_form_dict = v1beta1_json_web_key.from_dict(v1beta1_json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


