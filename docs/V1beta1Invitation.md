# V1beta1Invitation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique invitation identifier. | [optional] 
**user_id** | **str** | The user email of the invited user. | [optional] 
**org_id** | **str** | The organization id to which the user is invited. | [optional] 
**group_ids** | **List[str]** | The list of group ids to which the user is invited. | [optional] 
**metadata** | **object** | The metadata of the invitation. | [optional] 
**created_at** | **datetime** | The time when the invitation was created. | [optional] 
**expires_at** | **datetime** | The time when the invitation expires. | [optional] 
**role_ids** | **List[str]** | The list of role ids to which the user is invited in an organization. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_invitation import V1beta1Invitation

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Invitation from a JSON string
v1beta1_invitation_instance = V1beta1Invitation.from_json(json)
# print the JSON string representation of the object
print V1beta1Invitation.to_json()

# convert the object into a dict
v1beta1_invitation_dict = v1beta1_invitation_instance.to_dict()
# create an instance of V1beta1Invitation from a dict
v1beta1_invitation_form_dict = v1beta1_invitation.from_dict(v1beta1_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


