# shield_api.model.v1beta1_meta_schema.V1beta1MetaSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique metaschema uuid. | [optional] 
**name** | str,  | str,  |  | [optional] 
**schema** | str,  | str,  | The metaschema json schema. | [optional] 
**createdAt** | str, datetime,  | str,  | The time when the metaschema was created. | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  | The time when the metaschema was updated. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

