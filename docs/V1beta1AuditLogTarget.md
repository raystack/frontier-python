# V1beta1AuditLogTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_audit_log_target import V1beta1AuditLogTarget

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AuditLogTarget from a JSON string
v1beta1_audit_log_target_instance = V1beta1AuditLogTarget.from_json(json)
# print the JSON string representation of the object
print V1beta1AuditLogTarget.to_json()

# convert the object into a dict
v1beta1_audit_log_target_dict = v1beta1_audit_log_target_instance.to_dict()
# create an instance of V1beta1AuditLogTarget from a dict
v1beta1_audit_log_target_form_dict = v1beta1_audit_log_target.from_dict(v1beta1_audit_log_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


