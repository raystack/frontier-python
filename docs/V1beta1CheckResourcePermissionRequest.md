# V1beta1CheckResourcePermissionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** | Deprecated. Use &#x60;resource&#x60; field instead. | [optional] 
**object_namespace** | **str** | Deprecated. Use &#x60;resource&#x60; field instead. | [optional] 
**permission** | **str** | the permission name to check. &lt;br/&gt; *Example:* &#x60;get&#x60;, &#x60;list&#x60;, &#x60;compute.instance.create&#x60; | 
**resource** | **str** | &#x60;namespace:uuid&#x60; or &#x60;namespace:name&#x60; of the org or project, and &#x60;namespace:urn&#x60; of a resource under a project. In case of an org/project either provide the complete namespace (app/organization) or Frontier can also parse aliases for the same as &#x60;org&#x60; or &#x60;project&#x60;. &lt;br/&gt; *Example:* &#x60;organization:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; or &#x60;app/project:project-name&#x60; or &#x60;compute/instance:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | [optional] 

## Example

```python
from frontier_api.models.v1beta1_check_resource_permission_request import V1beta1CheckResourcePermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CheckResourcePermissionRequest from a JSON string
v1beta1_check_resource_permission_request_instance = V1beta1CheckResourcePermissionRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1CheckResourcePermissionRequest.to_json()

# convert the object into a dict
v1beta1_check_resource_permission_request_dict = v1beta1_check_resource_permission_request_instance.to_dict()
# create an instance of V1beta1CheckResourcePermissionRequest from a dict
v1beta1_check_resource_permission_request_form_dict = v1beta1_check_resource_permission_request.from_dict(v1beta1_check_resource_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


