# FrontierServiceCreateOrganizationDomainRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | domain name to be added to the trusted domain list | 

## Example

```python
from frontier_api.models.frontier_service_create_organization_domain_request import FrontierServiceCreateOrganizationDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceCreateOrganizationDomainRequest from a JSON string
frontier_service_create_organization_domain_request_instance = FrontierServiceCreateOrganizationDomainRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceCreateOrganizationDomainRequest.to_json()

# convert the object into a dict
frontier_service_create_organization_domain_request_dict = frontier_service_create_organization_domain_request_instance.to_dict()
# create an instance of FrontierServiceCreateOrganizationDomainRequest from a dict
frontier_service_create_organization_domain_request_form_dict = frontier_service_create_organization_domain_request.from_dict(frontier_service_create_organization_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


