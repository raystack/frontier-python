# V1beta1ListUserGroupsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[V1beta1Group]**](V1beta1Group.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_user_groups_response import V1beta1ListUserGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListUserGroupsResponse from a JSON string
v1beta1_list_user_groups_response_instance = V1beta1ListUserGroupsResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListUserGroupsResponse.to_json()

# convert the object into a dict
v1beta1_list_user_groups_response_dict = v1beta1_list_user_groups_response_instance.to_dict()
# create an instance of V1beta1ListUserGroupsResponse from a dict
v1beta1_list_user_groups_response_form_dict = v1beta1_list_user_groups_response.from_dict(v1beta1_list_user_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


