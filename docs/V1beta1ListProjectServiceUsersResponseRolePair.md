# V1beta1ListProjectServiceUsersResponseRolePair


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceuser_id** | **str** |  | [optional] 
**roles** | [**List[V1beta1Role]**](V1beta1Role.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_project_service_users_response_role_pair import V1beta1ListProjectServiceUsersResponseRolePair

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListProjectServiceUsersResponseRolePair from a JSON string
v1beta1_list_project_service_users_response_role_pair_instance = V1beta1ListProjectServiceUsersResponseRolePair.from_json(json)
# print the JSON string representation of the object
print V1beta1ListProjectServiceUsersResponseRolePair.to_json()

# convert the object into a dict
v1beta1_list_project_service_users_response_role_pair_dict = v1beta1_list_project_service_users_response_role_pair_instance.to_dict()
# create an instance of V1beta1ListProjectServiceUsersResponseRolePair from a dict
v1beta1_list_project_service_users_response_role_pair_form_dict = v1beta1_list_project_service_users_response_role_pair.from_dict(v1beta1_list_project_service_users_response_role_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


