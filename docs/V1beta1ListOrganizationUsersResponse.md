# V1beta1ListOrganizationUsersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[V1beta1User]**](V1beta1User.md) |  | [optional] 
**role_pairs** | [**List[V1beta1ListOrganizationUsersResponseRolePair]**](V1beta1ListOrganizationUsersResponseRolePair.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_organization_users_response import V1beta1ListOrganizationUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListOrganizationUsersResponse from a JSON string
v1beta1_list_organization_users_response_instance = V1beta1ListOrganizationUsersResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListOrganizationUsersResponse.to_json()

# convert the object into a dict
v1beta1_list_organization_users_response_dict = v1beta1_list_organization_users_response_instance.to_dict()
# create an instance of V1beta1ListOrganizationUsersResponse from a dict
v1beta1_list_organization_users_response_form_dict = v1beta1_list_organization_users_response.from_dict(v1beta1_list_organization_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


