# V1beta1UserRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the user. The name must be unique within the entire Frontier instance. The name can contain only alphanumeric characters, dashes and underscores and must start with a letter. If not provided, Frontier automatically generates a name from the user email.  | [optional] 
**email** | **str** | The email of the user. The email must be unique within the entire Frontier instance.&lt;br/&gt;*Example:*&#x60;\&quot;john.doe@raystack.org\&quot;&#x60; | 
**metadata** | **object** | Metadata object for users that can hold key value pairs pre-defined in User Metaschema. The metadata object can be used to store arbitrary information about the user such as label, description etc. By default the user metaschema contains labels and descriptions for the user. Update the same to add more fields to the user metadata object. &lt;br/&gt;*Example:*&#x60;{\&quot;label\&quot;: {\&quot;key1\&quot;: \&quot;value1\&quot;}, \&quot;description\&quot;: \&quot;User Description\&quot;}&#x60; | [optional] 
**title** | **str** | The title can contain any UTF-8 character, used to provide a human-readable name for the user. Can also be left empty. &lt;br/&gt;*Example:*&#x60;\&quot;John Doe\&quot;&#x60; | [optional] 
**avatar** | **str** | The avatar is base64 encoded image data of the user. Can also be left empty. The image should be less than 200KB. Should follow the regex pattern &#x60;^data:image/(png|jpg|jpeg|gif);base64,([a-zA-Z0-9+/]+&#x3D;{0,2})+$&#x60;. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_user_request_body import V1beta1UserRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1UserRequestBody from a JSON string
v1beta1_user_request_body_instance = V1beta1UserRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1UserRequestBody.to_json()

# convert the object into a dict
v1beta1_user_request_body_dict = v1beta1_user_request_body_instance.to_dict()
# create an instance of V1beta1UserRequestBody from a dict
v1beta1_user_request_body_form_dict = v1beta1_user_request_body.from_dict(v1beta1_user_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


