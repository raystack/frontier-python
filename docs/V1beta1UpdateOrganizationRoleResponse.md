# V1beta1UpdateOrganizationRoleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**V1beta1Role**](V1beta1Role.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_update_organization_role_response import V1beta1UpdateOrganizationRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1UpdateOrganizationRoleResponse from a JSON string
v1beta1_update_organization_role_response_instance = V1beta1UpdateOrganizationRoleResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1UpdateOrganizationRoleResponse.to_json()

# convert the object into a dict
v1beta1_update_organization_role_response_dict = v1beta1_update_organization_role_response_instance.to_dict()
# create an instance of V1beta1UpdateOrganizationRoleResponse from a dict
v1beta1_update_organization_role_response_form_dict = v1beta1_update_organization_role_response.from_dict(v1beta1_update_organization_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

