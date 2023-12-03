# V1beta1GetOrganizationInvitationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation** | [**V1beta1Invitation**](V1beta1Invitation.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_organization_invitation_response import V1beta1GetOrganizationInvitationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetOrganizationInvitationResponse from a JSON string
v1beta1_get_organization_invitation_response_instance = V1beta1GetOrganizationInvitationResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetOrganizationInvitationResponse.to_json()

# convert the object into a dict
v1beta1_get_organization_invitation_response_dict = v1beta1_get_organization_invitation_response_instance.to_dict()
# create an instance of V1beta1GetOrganizationInvitationResponse from a dict
v1beta1_get_organization_invitation_response_form_dict = v1beta1_get_organization_invitation_response.from_dict(v1beta1_get_organization_invitation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


