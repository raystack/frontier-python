# V1beta1UpdateRoleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**V1beta1Role**](V1beta1Role.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_update_role_response import V1beta1UpdateRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1UpdateRoleResponse from a JSON string
v1beta1_update_role_response_instance = V1beta1UpdateRoleResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1UpdateRoleResponse.to_json()

# convert the object into a dict
v1beta1_update_role_response_dict = v1beta1_update_role_response_instance.to_dict()
# create an instance of V1beta1UpdateRoleResponse from a dict
v1beta1_update_role_response_form_dict = v1beta1_update_role_response.from_dict(v1beta1_update_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


