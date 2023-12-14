# V1beta1CreateProjectResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**V1beta1Project**](V1beta1Project.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_create_project_response import V1beta1CreateProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CreateProjectResponse from a JSON string
v1beta1_create_project_response_instance = V1beta1CreateProjectResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1CreateProjectResponse.to_json()

# convert the object into a dict
v1beta1_create_project_response_dict = v1beta1_create_project_response_instance.to_dict()
# create an instance of V1beta1CreateProjectResponse from a dict
v1beta1_create_project_response_form_dict = v1beta1_create_project_response.from_dict(v1beta1_create_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


