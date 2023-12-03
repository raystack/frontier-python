# V1beta1OrganizationRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the organization. The name must be unique within the entire Frontier instance. The name can contain only alphanumeric characters, dashes and underscores.&lt;br/&gt;*Example:*&#x60;\&quot;frontier-org1-acme\&quot;&#x60; | 
**title** | **str** | The title can contain any UTF-8 character, used to provide a human-readable name for the organization. Can also be left empty.&lt;br/&gt; *Example*: &#x60;\&quot;Acme Inc\&quot;&#x60; | [optional] 
**metadata** | **object** | Metadata object for organizations that can hold key value pairs defined in Organization Metaschema. The metadata object can be used to store arbitrary information about the organization such as labels, descriptions etc. The default Organization Metaschema contains labels and descripton fields. Update the Organization Metaschema to add more fields. &lt;br/&gt;*Example*:&#x60;{\&quot;labels\&quot;: {\&quot;key\&quot;: \&quot;value\&quot;}, \&quot;description\&quot;: \&quot;Organization description\&quot;}&#x60; | [optional] 
**avatar** | **str** | The avatar is base64 encoded image data of the user. Can also be left empty. The image should be less than 200KB. Should follow the regex pattern &#x60;^data:image/(png|jpg|jpeg|gif);base64,([a-zA-Z0-9+/]+&#x3D;{0,2})+$&#x60;. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_organization_request_body import V1beta1OrganizationRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1OrganizationRequestBody from a JSON string
v1beta1_organization_request_body_instance = V1beta1OrganizationRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1OrganizationRequestBody.to_json()

# convert the object into a dict
v1beta1_organization_request_body_dict = v1beta1_organization_request_body_instance.to_dict()
# create an instance of V1beta1OrganizationRequestBody from a dict
v1beta1_organization_request_body_form_dict = v1beta1_organization_request_body.from_dict(v1beta1_organization_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


