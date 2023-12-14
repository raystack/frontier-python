# V1beta1UpdateFeatureResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**V1beta1Feature**](V1beta1Feature.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_update_feature_response import V1beta1UpdateFeatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1UpdateFeatureResponse from a JSON string
v1beta1_update_feature_response_instance = V1beta1UpdateFeatureResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1UpdateFeatureResponse.to_json()

# convert the object into a dict
v1beta1_update_feature_response_dict = v1beta1_update_feature_response_instance.to_dict()
# create an instance of V1beta1UpdateFeatureResponse from a dict
v1beta1_update_feature_response_form_dict = v1beta1_update_feature_response.from_dict(v1beta1_update_feature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


