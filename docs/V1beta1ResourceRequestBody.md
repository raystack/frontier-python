# V1beta1ResourceRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource.  Must be unique within the project. &lt;br/&gt; *Example:* &#x60;my-resource&#x60; | 
**title** | **str** | The title can contain any UTF-8 character, used to provide a human-readable name for the resource. Can also be left empty. | [optional] 
**namespace** | **str** | The namespace of the resource. The resource namespace are created when permissions for that resource is created in Frontier. If namespace doesn&#39;t exists the request will fail. &lt;br/&gt; *Example:* &#x60;compute/instance&#x60; | 
**principal** | **str** | UserID or ServiceUserID that should be marked as owner of the resource. If not provided, the current logged in user will be made the resource owner. &lt;br/&gt; *Example:* &#x60;user:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_resource_request_body import V1beta1ResourceRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ResourceRequestBody from a JSON string
v1beta1_resource_request_body_instance = V1beta1ResourceRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1ResourceRequestBody.to_json()

# convert the object into a dict
v1beta1_resource_request_body_dict = v1beta1_resource_request_body_instance.to_dict()
# create an instance of V1beta1ResourceRequestBody from a dict
v1beta1_resource_request_body_form_dict = v1beta1_resource_request_body.from_dict(v1beta1_resource_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


