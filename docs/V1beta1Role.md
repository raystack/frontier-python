# V1beta1Role


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** | The time the role was created. | [optional] 
**updated_at** | **datetime** | The time the role was last updated. | [optional] 
**org_id** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_role import V1beta1Role

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Role from a JSON string
v1beta1_role_instance = V1beta1Role.from_json(json)
# print the JSON string representation of the object
print V1beta1Role.to_json()

# convert the object into a dict
v1beta1_role_dict = v1beta1_role_instance.to_dict()
# create an instance of V1beta1Role from a dict
v1beta1_role_form_dict = v1beta1_role.from_dict(v1beta1_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


