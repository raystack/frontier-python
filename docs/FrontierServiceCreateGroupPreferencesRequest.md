# FrontierServiceCreateGroupPreferencesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bodies** | [**List[V1beta1PreferenceRequestBody]**](V1beta1PreferenceRequestBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_create_group_preferences_request import FrontierServiceCreateGroupPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceCreateGroupPreferencesRequest from a JSON string
frontier_service_create_group_preferences_request_instance = FrontierServiceCreateGroupPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceCreateGroupPreferencesRequest.to_json()

# convert the object into a dict
frontier_service_create_group_preferences_request_dict = frontier_service_create_group_preferences_request_instance.to_dict()
# create an instance of FrontierServiceCreateGroupPreferencesRequest from a dict
frontier_service_create_group_preferences_request_form_dict = frontier_service_create_group_preferences_request.from_dict(frontier_service_create_group_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


