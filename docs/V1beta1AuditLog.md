# V1beta1AuditLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source** | **str** | The source service generating the event. | 
**action** | **str** |  | 
**actor** | [**V1beta1AuditLogActor**](V1beta1AuditLogActor.md) |  | [optional] 
**target** | [**V1beta1AuditLogTarget**](V1beta1AuditLogTarget.md) |  | [optional] 
**context** | **Dict[str, str]** |  | [optional] 
**created_at** | **datetime** | The time the log was created. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_audit_log import V1beta1AuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AuditLog from a JSON string
v1beta1_audit_log_instance = V1beta1AuditLog.from_json(json)
# print the JSON string representation of the object
print V1beta1AuditLog.to_json()

# convert the object into a dict
v1beta1_audit_log_dict = v1beta1_audit_log_instance.to_dict()
# create an instance of V1beta1AuditLog from a dict
v1beta1_audit_log_form_dict = v1beta1_audit_log.from_dict(v1beta1_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


