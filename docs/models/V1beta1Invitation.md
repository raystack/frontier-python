# frontier_api.model.v1beta1_invitation.V1beta1Invitation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique invitation identifier. | [optional] 
**userId** | str,  | str,  | The user email of the invited user. | [optional] 
**orgId** | str,  | str,  | The organization id to which the user is invited. | [optional] 
**[groupIds](#groupIds)** | list, tuple,  | tuple,  | The list of group ids to which the user is invited. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata of the invitation. | [optional] 
**createdAt** | str, datetime,  | str,  | The time when the invitation was created. | [optional] value must conform to RFC-3339 date-time
**expiresAt** | str, datetime,  | str,  | The time when the invitation expires. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# groupIds

The list of group ids to which the user is invited.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of group ids to which the user is invited. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# metadata

The metadata of the invitation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata of the invitation. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

