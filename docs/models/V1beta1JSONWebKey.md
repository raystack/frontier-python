# shield_api.model.v1beta1_json_web_key.V1beta1JSONWebKey

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kty** | str,  | str,  | Key Type. | [optional] 
**alg** | str,  | str,  | Algorithm. | [optional] 
**use** | str,  | str,  | Permitted uses for the public keys. | [optional] 
**kid** | str,  | str,  | Key ID. | [optional] 
**n** | str,  | str,  | Used for RSA keys. | [optional] 
**e** | str,  | str,  | Used for RSA keys. | [optional] 
**x** | str,  | str,  | Used for ECDSA keys. | [optional] 
**y** | str,  | str,  | Used for ECDSA keys. | [optional] 
**crv** | str,  | str,  | Used for ECDSA keys. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

