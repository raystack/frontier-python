# V1beta1ListProjectsByCurrentUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[V1beta1Project]**](V1beta1Project.md) |  | [optional] 
**access_pairs** | [**List[V1beta1ListProjectsByCurrentUserResponseAccessPair]**](V1beta1ListProjectsByCurrentUserResponseAccessPair.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_projects_by_current_user_response import V1beta1ListProjectsByCurrentUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListProjectsByCurrentUserResponse from a JSON string
v1beta1_list_projects_by_current_user_response_instance = V1beta1ListProjectsByCurrentUserResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListProjectsByCurrentUserResponse.to_json()

# convert the object into a dict
v1beta1_list_projects_by_current_user_response_dict = v1beta1_list_projects_by_current_user_response_instance.to_dict()
# create an instance of V1beta1ListProjectsByCurrentUserResponse from a dict
v1beta1_list_projects_by_current_user_response_form_dict = v1beta1_list_projects_by_current_user_response.from_dict(v1beta1_list_projects_by_current_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


