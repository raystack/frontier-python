# V1beta1PermissionRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the permission. It should be unique across a Frontier instance and can contain only alphanumeric characters. | [optional] 
**namespace** | **str** | The namespace of the permission. The namespace should be in service/resource format.&lt;br/&gt;*Example:*&#x60;compute/guardian&#x60; | [optional] 
**metadata** | **object** | The metadata object for permissions that can hold key value pairs. | [optional] 
**title** | **str** | The title can contain any UTF-8 character, used to provide a human-readable name for the permissions. Can also be left empty. | [optional] 
**key** | **str** | Permission path key is composed of three parts, &#39;service.resource.verb&#39;. Where &#39;service.resource&#39; works as a namespace for the &#39;verb&#39;. Namespace name cannot be &#x60;app&#x60; as it&#39;s reserved for core permissions. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_permission_request_body import V1beta1PermissionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PermissionRequestBody from a JSON string
v1beta1_permission_request_body_instance = V1beta1PermissionRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1PermissionRequestBody.to_json()

# convert the object into a dict
v1beta1_permission_request_body_dict = v1beta1_permission_request_body_instance.to_dict()
# create an instance of V1beta1PermissionRequestBody from a dict
v1beta1_permission_request_body_form_dict = v1beta1_permission_request_body.from_dict(v1beta1_permission_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


