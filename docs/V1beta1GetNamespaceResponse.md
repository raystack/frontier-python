# V1beta1GetNamespaceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | [**V1beta1Namespace**](V1beta1Namespace.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_namespace_response import V1beta1GetNamespaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetNamespaceResponse from a JSON string
v1beta1_get_namespace_response_instance = V1beta1GetNamespaceResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetNamespaceResponse.to_json()

# convert the object into a dict
v1beta1_get_namespace_response_dict = v1beta1_get_namespace_response_instance.to_dict()
# create an instance of V1beta1GetNamespaceResponse from a dict
v1beta1_get_namespace_response_form_dict = v1beta1_get_namespace_response.from_dict(v1beta1_get_namespace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


