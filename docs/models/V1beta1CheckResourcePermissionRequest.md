# shield_api.model.v1beta1_check_resource_permission_request.V1beta1CheckResourcePermissionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**permission** | str,  | str,  | the permission name to check. &lt;br/&gt; *Example:* &#x60;get&#x60; or &#x60;list&#x60; | 
**objectId** | str,  | str,  | Deprecated. Use &#x60;resource&#x60; field instead. | [optional] 
**objectNamespace** | str,  | str,  | Deprecated. Use &#x60;resource&#x60; field instead. | [optional] 
**resource** | str,  | str,  | &#x60;namespace:uuid&#x60; or &#x60;namespace:name&#x60; of the org or project, and &#x60;namespace:urn&#x60; of a resource under a project. In case of an org/project either provide the complete namespace (app/organization) or Shield can also parse aliases for the same as &#x60;org&#x60; or &#x60;project&#x60;. &lt;br/&gt; *Example:* &#x60;organization:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; or &#x60;app/project:project-name&#x60; or &#x60;compute/instance:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

