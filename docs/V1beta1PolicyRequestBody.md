# V1beta1PolicyRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | unique id of the role to which policy is assigned | 
**title** | **str** | The title can contain any UTF-8 character, used to provide a human-readable name for the policy. Can also be left empty. &lt;br/&gt; *Example:* &#x60;Policy title&#x60; | [optional] 
**resource** | **str** | The resource to which policy is assigned in this format &#x60;namespace:uuid&#x60;. &lt;br/&gt; *Example:* &#x60;app/guardian:70f69c3a-334b-4f25-90b8-4d4f3be6b8e2&#x60; | 
**principal** | **str** | principal is the user or group to which policy is assigned. The principal id must be prefixed with its namespace id in this format &#x60;namespace:uuid&#x60;. The namespace can be &#x60;app/user&#x60;, &#x60;app/group&#x60; or &#x60;app/serviceuser&#x60; (coming up!) and uuid is the unique id of the principal. &lt;br/&gt; *Example:* &#x60;app/user:92f69c3a-334b-4f25-90b8-4d4f3be6b825&#x60; | 
**metadata** | **object** | Metadata object for policies that can hold key value pairs defined in Policy Metaschema.&lt;br/&gt; *Example:* &#x60;{\&quot;labels\&quot;: {\&quot;key\&quot;: \&quot;value\&quot;}, \&quot;description\&quot;: \&quot;Policy description\&quot;}&#x60; | [optional] 

## Example

```python
from frontier_api.models.v1beta1_policy_request_body import V1beta1PolicyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PolicyRequestBody from a JSON string
v1beta1_policy_request_body_instance = V1beta1PolicyRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1PolicyRequestBody.to_json()

# convert the object into a dict
v1beta1_policy_request_body_dict = v1beta1_policy_request_body_instance.to_dict()
# create an instance of V1beta1PolicyRequestBody from a dict
v1beta1_policy_request_body_form_dict = v1beta1_policy_request_body.from_dict(v1beta1_policy_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


