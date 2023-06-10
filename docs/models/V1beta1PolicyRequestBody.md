# shield_api.model.v1beta1_policy_request_body.V1beta1PolicyRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**principal** | str,  | str,  | principal is the user or group to which policy is assigned. The principal id must be prefixed with its namespace id in this format &#x60;namespace:uuid&#x60;. The namespace can be &#x60;app/user&#x60;, &#x60;app/group&#x60; or &#x60;app/serviceuser&#x60; (coming up!) and uuid is the unique id of the principal. &lt;br/&gt; *Example:* &#x60;app/user:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | 
**resource** | str,  | str,  | The resource to which policy is assigned in this format &#x60;namespace:uuid&#x60;. &lt;br/&gt; *Example:* &#x60;app/guardian:70f69c3a-334b-4f25-90b8-4d4f3be6b8e2&#x60; | 
**roleId** | str,  | str,  | unique id of the role to which policy is assigned | 
**title** | str,  | str,  | The title can contain any UTF-8 character, used to provide a human-readable name for the policy. Can also be left empty. &lt;br/&gt; *Example:* &#x60;Policy title&#x60; | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for policies that can hold key value pairs defined in Policy Metaschema.&lt;br/&gt; *Example:* &#x60;{\&quot;labels\&quot;: {\&quot;key\&quot;: \&quot;value\&quot;}, \&quot;description\&quot;: \&quot;Policy description\&quot;}&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Metadata object for policies that can hold key value pairs defined in Policy Metaschema.<br/> *Example:* `{\"labels\": {\"key\": \"value\"}, \"description\": \"Policy description\"}`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for policies that can hold key value pairs defined in Policy Metaschema.&lt;br/&gt; *Example:* &#x60;{\&quot;labels\&quot;: {\&quot;key\&quot;: \&quot;value\&quot;}, \&quot;description\&quot;: \&quot;Policy description\&quot;}&#x60; | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

