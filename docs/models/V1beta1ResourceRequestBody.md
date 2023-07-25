# shield_api.model.v1beta1_resource_request_body.V1beta1ResourceRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the resource.  Must be unique within the project. &lt;br/&gt; *Example:* &#x60;my-resource&#x60; | 
**namespace** | str,  | str,  | The namespace of the resource. The resource namespace are created when permissions for that resource is created in Shield. If namespace doesn&#x27;t exists the request will fail. &lt;br/&gt; *Example:* &#x60;compute/instance&#x60; | 
**title** | str,  | str,  | The title can contain any UTF-8 character, used to provide a human-readable name for the resource. Can also be left empty. | [optional] 
**principal** | str,  | str,  | UserID or ServiceUserID that should be marked as owner of the resource. If not provided, the current logged in user will be made the resource owner. &lt;br/&gt; *Example:* &#x60;user:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

