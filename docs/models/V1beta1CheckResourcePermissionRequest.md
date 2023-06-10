# shield_api.model.v1beta1_check_resource_permission_request.V1beta1CheckResourcePermissionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**permission** | str,  | str,  |  | 
**objectId** | str,  | str,  |  | [optional] 
**objectNamespace** | str,  | str,  |  | [optional] 
**resource** | str,  | str,  | namespace:uuid of the resource. &lt;br/&gt; *Example:* &#x60;organization:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

