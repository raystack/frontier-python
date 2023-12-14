# V1beta1ListOrganizationsByUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[V1beta1Organization]**](V1beta1Organization.md) |  | [optional] 
**joinable_via_domain** | [**List[V1beta1Organization]**](V1beta1Organization.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_organizations_by_user_response import V1beta1ListOrganizationsByUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListOrganizationsByUserResponse from a JSON string
v1beta1_list_organizations_by_user_response_instance = V1beta1ListOrganizationsByUserResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListOrganizationsByUserResponse.to_json()

# convert the object into a dict
v1beta1_list_organizations_by_user_response_dict = v1beta1_list_organizations_by_user_response_instance.to_dict()
# create an instance of V1beta1ListOrganizationsByUserResponse from a dict
v1beta1_list_organizations_by_user_response_form_dict = v1beta1_list_organizations_by_user_response.from_dict(v1beta1_list_organizations_by_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


