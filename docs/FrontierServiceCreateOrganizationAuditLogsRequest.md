# FrontierServiceCreateOrganizationAuditLogsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[V1beta1AuditLog]**](V1beta1AuditLog.md) |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_create_organization_audit_logs_request import FrontierServiceCreateOrganizationAuditLogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceCreateOrganizationAuditLogsRequest from a JSON string
frontier_service_create_organization_audit_logs_request_instance = FrontierServiceCreateOrganizationAuditLogsRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceCreateOrganizationAuditLogsRequest.to_json()

# convert the object into a dict
frontier_service_create_organization_audit_logs_request_dict = frontier_service_create_organization_audit_logs_request_instance.to_dict()
# create an instance of FrontierServiceCreateOrganizationAuditLogsRequest from a dict
frontier_service_create_organization_audit_logs_request_form_dict = frontier_service_create_organization_audit_logs_request.from_dict(frontier_service_create_organization_audit_logs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


