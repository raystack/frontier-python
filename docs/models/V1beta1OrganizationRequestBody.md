# shield_api.model.v1beta1_organization_request_body.V1beta1OrganizationRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the organization. The name must be unique within the entire Shield instance. The name can contain only alphanumeric characters, dashes and underscores.&lt;br/&gt;*Example:*&#x60;\&quot;shield-org1-acme\&quot;&#x60; | 
**title** | str,  | str,  | The title can contain any UTF-8 character, used to provide a human-readable name for the organization. Can also be left empty.&lt;br/&gt; *Example*: &#x60;\&quot;Acme Inc\&quot;&#x60; | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for organizations that can hold key value pairs defined in Organization Metaschema. The metadata object can be used to store arbitrary information about the organization such as labels, descriptions etc. The default Organization Metaschema contains labels and descripton fields. Update the Organization Metaschema to add more fields. &lt;br/&gt;*Example*:&#x60;{\&quot;labels\&quot;: {\&quot;key\&quot;: \&quot;value\&quot;}, \&quot;description\&quot;: \&quot;Organization description\&quot;}&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Metadata object for organizations that can hold key value pairs defined in Organization Metaschema. The metadata object can be used to store arbitrary information about the organization such as labels, descriptions etc. The default Organization Metaschema contains labels and descripton fields. Update the Organization Metaschema to add more fields. <br/>*Example*:`{\"labels\": {\"key\": \"value\"}, \"description\": \"Organization description\"}`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata object for organizations that can hold key value pairs defined in Organization Metaschema. The metadata object can be used to store arbitrary information about the organization such as labels, descriptions etc. The default Organization Metaschema contains labels and descripton fields. Update the Organization Metaschema to add more fields. &lt;br/&gt;*Example*:&#x60;{\&quot;labels\&quot;: {\&quot;key\&quot;: \&quot;value\&quot;}, \&quot;description\&quot;: \&quot;Organization description\&quot;}&#x60; | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

