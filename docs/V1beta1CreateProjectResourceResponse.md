# V1beta1CreateProjectResourceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**V1beta1Resource**](V1beta1Resource.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_create_project_resource_response import V1beta1CreateProjectResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CreateProjectResourceResponse from a JSON string
v1beta1_create_project_resource_response_instance = V1beta1CreateProjectResourceResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1CreateProjectResourceResponse.to_json()

# convert the object into a dict
v1beta1_create_project_resource_response_dict = v1beta1_create_project_resource_response_instance.to_dict()
# create an instance of V1beta1CreateProjectResourceResponse from a dict
v1beta1_create_project_resource_response_form_dict = v1beta1_create_project_resource_response.from_dict(v1beta1_create_project_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


