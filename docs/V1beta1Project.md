# V1beta1Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** | The time the project was created. | [optional] 
**updated_at** | **datetime** | The time the project was last updated. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_project import V1beta1Project

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Project from a JSON string
v1beta1_project_instance = V1beta1Project.from_json(json)
# print the JSON string representation of the object
print V1beta1Project.to_json()

# convert the object into a dict
v1beta1_project_dict = v1beta1_project_instance.to_dict()
# create an instance of V1beta1Project from a dict
v1beta1_project_form_dict = v1beta1_project.from_dict(v1beta1_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


