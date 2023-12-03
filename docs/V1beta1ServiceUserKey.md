# V1beta1ServiceUserKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**principal_id** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** | The time when the secret was created. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_service_user_key import V1beta1ServiceUserKey

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ServiceUserKey from a JSON string
v1beta1_service_user_key_instance = V1beta1ServiceUserKey.from_json(json)
# print the JSON string representation of the object
print V1beta1ServiceUserKey.to_json()

# convert the object into a dict
v1beta1_service_user_key_dict = v1beta1_service_user_key_instance.to_dict()
# create an instance of V1beta1ServiceUserKey from a dict
v1beta1_service_user_key_form_dict = v1beta1_service_user_key.from_dict(v1beta1_service_user_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


