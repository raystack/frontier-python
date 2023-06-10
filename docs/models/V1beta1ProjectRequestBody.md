# shield_api.model.v1beta1_project_request_body.V1beta1ProjectRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the project. The name must be unique within the entire Shield instance. The name can contain only alphanumeric characters, dashes and underscores.&lt;br/&gt; *Example:* &#x60;shield-playground&#x60; | 
**orgId** | str,  | str,  | unique id of the organization to which project belongs | 
**title** | str,  | str,  | The title can contain any UTF-8 character, used to provide a human-readable name for the project. Can also be left empty. &lt;br/&gt; *Example:* &#x60;Shield Playground&#x60; | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for projects that can hold key value pairs defined in Project Metaschema. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Metadata object for projects that can hold key value pairs defined in Project Metaschema.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for projects that can hold key value pairs defined in Project Metaschema. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

