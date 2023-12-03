# V1beta1ProjectRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the project. The name must be unique within the entire Frontier instance. The name can contain only alphanumeric characters, dashes and underscores.&lt;br/&gt; *Example:* &#x60;frontier-playground&#x60; | 
**title** | **str** | The title can contain any UTF-8 character, used to provide a human-readable name for the project. Can also be left empty. &lt;br/&gt; *Example:* &#x60;Frontier Playground&#x60; | [optional] 
**metadata** | **object** | Metadata object for projects that can hold key value pairs defined in Project Metaschema. | [optional] 
**org_id** | **str** | unique id of the organization to which project belongs | 

## Example

```python
from frontier_api.models.v1beta1_project_request_body import V1beta1ProjectRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ProjectRequestBody from a JSON string
v1beta1_project_request_body_instance = V1beta1ProjectRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1ProjectRequestBody.to_json()

# convert the object into a dict
v1beta1_project_request_body_dict = v1beta1_project_request_body_instance.to_dict()
# create an instance of V1beta1ProjectRequestBody from a dict
v1beta1_project_request_body_form_dict = v1beta1_project_request_body.from_dict(v1beta1_project_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


