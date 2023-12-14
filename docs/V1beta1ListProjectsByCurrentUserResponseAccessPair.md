# V1beta1ListProjectsByCurrentUserResponseAccessPair


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_projects_by_current_user_response_access_pair import V1beta1ListProjectsByCurrentUserResponseAccessPair

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListProjectsByCurrentUserResponseAccessPair from a JSON string
v1beta1_list_projects_by_current_user_response_access_pair_instance = V1beta1ListProjectsByCurrentUserResponseAccessPair.from_json(json)
# print the JSON string representation of the object
print V1beta1ListProjectsByCurrentUserResponseAccessPair.to_json()

# convert the object into a dict
v1beta1_list_projects_by_current_user_response_access_pair_dict = v1beta1_list_projects_by_current_user_response_access_pair_instance.to_dict()
# create an instance of V1beta1ListProjectsByCurrentUserResponseAccessPair from a dict
v1beta1_list_projects_by_current_user_response_access_pair_form_dict = v1beta1_list_projects_by_current_user_response_access_pair.from_dict(v1beta1_list_projects_by_current_user_response_access_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


