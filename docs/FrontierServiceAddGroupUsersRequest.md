# FrontierServiceAddGroupUsersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_add_group_users_request import FrontierServiceAddGroupUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceAddGroupUsersRequest from a JSON string
frontier_service_add_group_users_request_instance = FrontierServiceAddGroupUsersRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceAddGroupUsersRequest.to_json()

# convert the object into a dict
frontier_service_add_group_users_request_dict = frontier_service_add_group_users_request_instance.to_dict()
# create an instance of FrontierServiceAddGroupUsersRequest from a dict
frontier_service_add_group_users_request_form_dict = frontier_service_add_group_users_request.from_dict(frontier_service_add_group_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


