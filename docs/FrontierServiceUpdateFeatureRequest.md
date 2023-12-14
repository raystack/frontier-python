# FrontierServiceUpdateFeatureRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**V1beta1FeatureRequestBody**](V1beta1FeatureRequestBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_update_feature_request import FrontierServiceUpdateFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceUpdateFeatureRequest from a JSON string
frontier_service_update_feature_request_instance = FrontierServiceUpdateFeatureRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceUpdateFeatureRequest.to_json()

# convert the object into a dict
frontier_service_update_feature_request_dict = frontier_service_update_feature_request_instance.to_dict()
# create an instance of FrontierServiceUpdateFeatureRequest from a dict
frontier_service_update_feature_request_form_dict = frontier_service_update_feature_request.from_dict(frontier_service_update_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


