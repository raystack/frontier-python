# V1beta1BatchCheckPermissionResponsePair


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**V1beta1BatchCheckPermissionBody**](V1beta1BatchCheckPermissionBody.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_batch_check_permission_response_pair import V1beta1BatchCheckPermissionResponsePair

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1BatchCheckPermissionResponsePair from a JSON string
v1beta1_batch_check_permission_response_pair_instance = V1beta1BatchCheckPermissionResponsePair.from_json(json)
# print the JSON string representation of the object
print V1beta1BatchCheckPermissionResponsePair.to_json()

# convert the object into a dict
v1beta1_batch_check_permission_response_pair_dict = v1beta1_batch_check_permission_response_pair_instance.to_dict()
# create an instance of V1beta1BatchCheckPermissionResponsePair from a dict
v1beta1_batch_check_permission_response_pair_form_dict = v1beta1_batch_check_permission_response_pair.from_dict(v1beta1_batch_check_permission_response_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


