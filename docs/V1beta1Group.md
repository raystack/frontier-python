# V1beta1Group


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** | The time the group was created. | [optional] 
**updated_at** | **datetime** | The time the group was last updated. | [optional] 
**users** | [**List[V1beta1User]**](V1beta1User.md) |  | [optional] [readonly] 
**members_count** | **int** | The number of members explicitly added in the project. | [optional] [readonly] 

## Example

```python
from frontier_api.models.v1beta1_group import V1beta1Group

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Group from a JSON string
v1beta1_group_instance = V1beta1Group.from_json(json)
# print the JSON string representation of the object
print V1beta1Group.to_json()

# convert the object into a dict
v1beta1_group_dict = v1beta1_group_instance.to_dict()
# create an instance of V1beta1Group from a dict
v1beta1_group_form_dict = v1beta1_group.from_dict(v1beta1_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


