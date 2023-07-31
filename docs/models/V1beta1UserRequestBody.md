# frontier_api.model.v1beta1_user_request_body.V1beta1UserRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email** | str,  | str,  | The email of the user. The email must be unique within the entire Frontier instance.&lt;br/&gt;*Example:*&#x60;\&quot;john.doe@raystack.org\&quot;&#x60; | 
**name** | str,  | str,  | The name of the user. The name must be unique within the entire Frontier instance. The name can contain only alphanumeric characters, dashes and underscores and must start with a letter. If not provided, Frontier automatically generates a name from the user email.  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for users that can hold key value pairs pre-defined in User Metaschema. The metadata object can be used to store arbitrary information about the user such as label, description etc. By default the user metaschema contains labels and descriptions for the user. Update the same to add more fields to the user metadata object. &lt;br/&gt;*Example:*&#x60;{\&quot;label\&quot;: {\&quot;key1\&quot;: \&quot;value1\&quot;}, \&quot;description\&quot;: \&quot;User Description\&quot;}&#x60; | [optional] 
**title** | str,  | str,  | The title can contain any UTF-8 character, used to provide a human-readable name for the user. Can also be left empty. &lt;br/&gt;*Example:*&#x60;\&quot;John Doe\&quot;&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Metadata object for users that can hold key value pairs pre-defined in User Metaschema. The metadata object can be used to store arbitrary information about the user such as label, description etc. By default the user metaschema contains labels and descriptions for the user. Update the same to add more fields to the user metadata object. <br/>*Example:*`{\"label\": {\"key1\": \"value1\"}, \"description\": \"User Description\"}`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for users that can hold key value pairs pre-defined in User Metaschema. The metadata object can be used to store arbitrary information about the user such as label, description etc. By default the user metaschema contains labels and descriptions for the user. Update the same to add more fields to the user metadata object. &lt;br/&gt;*Example:*&#x60;{\&quot;label\&quot;: {\&quot;key1\&quot;: \&quot;value1\&quot;}, \&quot;description\&quot;: \&quot;User Description\&quot;}&#x60; | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

