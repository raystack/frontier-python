# V1beta1GroupRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the group. The name must be unique within the entire Frontier instance. The name can contain only alphanumeric characters, dashes and underscores. | 
**title** | **str** | The title can contain any UTF-8 character, used to provide a human-readable name for the group. Can also be left empty. | [optional] 
**metadata** | **object** | Metadata object for groups that can hold key value pairs defined in Group Metaschema. The metadata object can be used to store arbitrary information about the group such as labels, descriptions etc. The default Group Metaschema contains labels and descripton fields. Update the Group Metaschema to add more fields.&lt;br/&gt;*Example:*&#x60;{\&quot;labels\&quot;: {\&quot;key\&quot;: \&quot;value\&quot;}, \&quot;description\&quot;: \&quot;Group description\&quot;}&#x60; | [optional] 

## Example

```python
from frontier_api.models.v1beta1_group_request_body import V1beta1GroupRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GroupRequestBody from a JSON string
v1beta1_group_request_body_instance = V1beta1GroupRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1GroupRequestBody.to_json()

# convert the object into a dict
v1beta1_group_request_body_dict = v1beta1_group_request_body_instance.to_dict()
# create an instance of V1beta1GroupRequestBody from a dict
v1beta1_group_request_body_form_dict = v1beta1_group_request_body.from_dict(v1beta1_group_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


