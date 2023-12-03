# V1beta1ListOrganizationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[V1beta1Organization]**](V1beta1Organization.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_organizations_response import V1beta1ListOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListOrganizationsResponse from a JSON string
v1beta1_list_organizations_response_instance = V1beta1ListOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListOrganizationsResponse.to_json()

# convert the object into a dict
v1beta1_list_organizations_response_dict = v1beta1_list_organizations_response_instance.to_dict()
# create an instance of V1beta1ListOrganizationsResponse from a dict
v1beta1_list_organizations_response_form_dict = v1beta1_list_organizations_response.from_dict(v1beta1_list_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


