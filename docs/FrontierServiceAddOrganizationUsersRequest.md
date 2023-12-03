# FrontierServiceAddOrganizationUsersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | List of user IDs to be added to the organization. | [optional] 

## Example

```python
from frontier_api.models.frontier_service_add_organization_users_request import FrontierServiceAddOrganizationUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceAddOrganizationUsersRequest from a JSON string
frontier_service_add_organization_users_request_instance = FrontierServiceAddOrganizationUsersRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceAddOrganizationUsersRequest.to_json()

# convert the object into a dict
frontier_service_add_organization_users_request_dict = frontier_service_add_organization_users_request_instance.to_dict()
# create an instance of FrontierServiceAddOrganizationUsersRequest from a dict
frontier_service_add_organization_users_request_form_dict = frontier_service_add_organization_users_request.from_dict(frontier_service_add_organization_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


