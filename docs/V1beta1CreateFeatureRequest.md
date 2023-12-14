# V1beta1CreateFeatureRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**V1beta1FeatureRequestBody**](V1beta1FeatureRequestBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_create_feature_request import V1beta1CreateFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CreateFeatureRequest from a JSON string
v1beta1_create_feature_request_instance = V1beta1CreateFeatureRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1CreateFeatureRequest.to_json()

# convert the object into a dict
v1beta1_create_feature_request_dict = v1beta1_create_feature_request_instance.to_dict()
# create an instance of V1beta1CreateFeatureRequest from a dict
v1beta1_create_feature_request_form_dict = v1beta1_create_feature_request.from_dict(v1beta1_create_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


