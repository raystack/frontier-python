# frontier_api.model.v1beta1_audit_log.V1beta1AuditLog

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**action** | str,  | str,  |  | 
**source** | str,  | str,  | The source service generating the event. | 
**id** | str,  | str,  |  | [optional] 
**actor** | [**V1beta1AuditLogActor**](V1beta1AuditLogActor.md) | [**V1beta1AuditLogActor**](V1beta1AuditLogActor.md) |  | [optional] 
**target** | [**V1beta1AuditLogTarget**](V1beta1AuditLogTarget.md) | [**V1beta1AuditLogTarget**](V1beta1AuditLogTarget.md) |  | [optional] 
**[context](#context)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**createdAt** | str, datetime,  | str,  | The time the log was created. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# context

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

