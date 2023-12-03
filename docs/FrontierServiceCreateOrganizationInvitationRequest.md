# FrontierServiceCreateOrganizationInvitationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | user_id is email id of user who are invited inside the organization. If user is not registered on the platform, it will be notified | 
**group_ids** | **List[str]** | list of group ids to which user needs to be added as a member. | [optional] 
**role_ids** | **List[str]** | list of role ids to which user needs to be added as a member. Roles are binded at organization level by default. | [optional] 

## Example

```python
from frontier_api.models.frontier_service_create_organization_invitation_request import FrontierServiceCreateOrganizationInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceCreateOrganizationInvitationRequest from a JSON string
frontier_service_create_organization_invitation_request_instance = FrontierServiceCreateOrganizationInvitationRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceCreateOrganizationInvitationRequest.to_json()

# convert the object into a dict
frontier_service_create_organization_invitation_request_dict = frontier_service_create_organization_invitation_request_instance.to_dict()
# create an instance of FrontierServiceCreateOrganizationInvitationRequest from a dict
frontier_service_create_organization_invitation_request_form_dict = frontier_service_create_organization_invitation_request.from_dict(frontier_service_create_organization_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


