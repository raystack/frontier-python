# V1beta1CreateCurrentUserPreferencesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**List[V1beta1Preference]**](V1beta1Preference.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_create_current_user_preferences_response import V1beta1CreateCurrentUserPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CreateCurrentUserPreferencesResponse from a JSON string
v1beta1_create_current_user_preferences_response_instance = V1beta1CreateCurrentUserPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1CreateCurrentUserPreferencesResponse.to_json()

# convert the object into a dict
v1beta1_create_current_user_preferences_response_dict = v1beta1_create_current_user_preferences_response_instance.to_dict()
# create an instance of V1beta1CreateCurrentUserPreferencesResponse from a dict
v1beta1_create_current_user_preferences_response_form_dict = v1beta1_create_current_user_preferences_response.from_dict(v1beta1_create_current_user_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


