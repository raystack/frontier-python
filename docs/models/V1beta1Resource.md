# shield_api.model.v1beta1_resource.V1beta1Resource

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  | Name of the resource. Must be unique within the project. | [optional] 
**createdAt** | str, datetime,  | str,  | The time the resource was created. | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  | The time the resource was last updated. | [optional] value must conform to RFC-3339 date-time
**urn** | str,  | str,  |  | [optional] 
**projectId** | str,  | str,  |  | [optional] 
**namespace** | str,  | str,  |  | [optional] 
**principal** | str,  | str,  |  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

