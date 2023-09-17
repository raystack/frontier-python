# frontier_api.model.v1beta1_user.V1beta1User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  | Unique name of the user. | [optional] 
**title** | str,  | str,  | Name of the user. | [optional] 
**email** | str,  | str,  |  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**createdAt** | str, datetime,  | str,  | The time the user was created. | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  | The time the user was last updated. | [optional] value must conform to RFC-3339 date-time
**state** | str,  | str,  | The state of the user (enabled or disabled). | [optional] 
**avatar** | str,  | str,  | The base64 encoded image string of the user avatar. Should be less than 2MB. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

