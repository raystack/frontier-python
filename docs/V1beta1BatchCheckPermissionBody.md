# V1beta1BatchCheckPermissionBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | the permission name to check. &lt;br/&gt; *Example:* &#x60;get&#x60; or &#x60;list&#x60; | 
**resource** | **str** | &#x60;namespace:uuid&#x60; or &#x60;namespace:name&#x60; of the org or project, and &#x60;namespace:urn&#x60; of a resource under a project. In case of an org/project either provide the complete namespace (app/organization) or Frontier can also parse aliases for the same as &#x60;org&#x60; or &#x60;project&#x60;. &lt;br/&gt; *Example:* &#x60;organization:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; or &#x60;app/project:project-name&#x60; or &#x60;compute/instance:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | [optional] 

## Example

```python
from frontier_api.models.v1beta1_batch_check_permission_body import V1beta1BatchCheckPermissionBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1BatchCheckPermissionBody from a JSON string
v1beta1_batch_check_permission_body_instance = V1beta1BatchCheckPermissionBody.from_json(json)
# print the JSON string representation of the object
print V1beta1BatchCheckPermissionBody.to_json()

# convert the object into a dict
v1beta1_batch_check_permission_body_dict = v1beta1_batch_check_permission_body_instance.to_dict()
# create an instance of V1beta1BatchCheckPermissionBody from a dict
v1beta1_batch_check_permission_body_form_dict = v1beta1_batch_check_permission_body.from_dict(v1beta1_batch_check_permission_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


