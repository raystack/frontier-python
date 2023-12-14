# V1beta1BatchCheckPermissionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bodies** | [**List[V1beta1BatchCheckPermissionBody]**](V1beta1BatchCheckPermissionBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_batch_check_permission_request import V1beta1BatchCheckPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1BatchCheckPermissionRequest from a JSON string
v1beta1_batch_check_permission_request_instance = V1beta1BatchCheckPermissionRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1BatchCheckPermissionRequest.to_json()

# convert the object into a dict
v1beta1_batch_check_permission_request_dict = v1beta1_batch_check_permission_request_instance.to_dict()
# create an instance of V1beta1BatchCheckPermissionRequest from a dict
v1beta1_batch_check_permission_request_form_dict = v1beta1_batch_check_permission_request.from_dict(v1beta1_batch_check_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


