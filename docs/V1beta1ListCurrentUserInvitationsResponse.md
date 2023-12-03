# V1beta1ListCurrentUserInvitationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[V1beta1Invitation]**](V1beta1Invitation.md) |  | [optional] 
**orgs** | [**List[V1beta1Organization]**](V1beta1Organization.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_current_user_invitations_response import V1beta1ListCurrentUserInvitationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListCurrentUserInvitationsResponse from a JSON string
v1beta1_list_current_user_invitations_response_instance = V1beta1ListCurrentUserInvitationsResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListCurrentUserInvitationsResponse.to_json()

# convert the object into a dict
v1beta1_list_current_user_invitations_response_dict = v1beta1_list_current_user_invitations_response_instance.to_dict()
# create an instance of V1beta1ListCurrentUserInvitationsResponse from a dict
v1beta1_list_current_user_invitations_response_form_dict = v1beta1_list_current_user_invitations_response.from_dict(v1beta1_list_current_user_invitations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


