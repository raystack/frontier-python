# V1beta1ListOrganizationDomainsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[V1beta1Domain]**](V1beta1Domain.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_organization_domains_response import V1beta1ListOrganizationDomainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListOrganizationDomainsResponse from a JSON string
v1beta1_list_organization_domains_response_instance = V1beta1ListOrganizationDomainsResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListOrganizationDomainsResponse.to_json()

# convert the object into a dict
v1beta1_list_organization_domains_response_dict = v1beta1_list_organization_domains_response_instance.to_dict()
# create an instance of V1beta1ListOrganizationDomainsResponse from a dict
v1beta1_list_organization_domains_response_form_dict = v1beta1_list_organization_domains_response.from_dict(v1beta1_list_organization_domains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


