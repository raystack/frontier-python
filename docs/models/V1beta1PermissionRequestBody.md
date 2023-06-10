# shield_api.model.v1beta1_permission_request_body.V1beta1PermissionRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the permission. It should be unique across a Shield instance and can contain only alphanumeric characters. | 
**namespace** | str,  | str,  | The namespace of the permission.The namespace should be in service/resource format.&lt;br/&gt;*Example:*&#x60;app/guardian&#x60; | 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata object for permissions that can hold key value pairs. | [optional] 
**title** | str,  | str,  | The title can contain any UTF-8 character, used to provide a human-readable name for the permissions. Can also be left empty. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

The metadata object for permissions that can hold key value pairs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata object for permissions that can hold key value pairs. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

