# V1beta1GetOrganizationAuditLogResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | [**V1beta1AuditLog**](V1beta1AuditLog.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_organization_audit_log_response import V1beta1GetOrganizationAuditLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetOrganizationAuditLogResponse from a JSON string
v1beta1_get_organization_audit_log_response_instance = V1beta1GetOrganizationAuditLogResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetOrganizationAuditLogResponse.to_json()

# convert the object into a dict
v1beta1_get_organization_audit_log_response_dict = v1beta1_get_organization_audit_log_response_instance.to_dict()
# create an instance of V1beta1GetOrganizationAuditLogResponse from a dict
v1beta1_get_organization_audit_log_response_form_dict = v1beta1_get_organization_audit_log_response.from_dict(v1beta1_get_organization_audit_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


