# V1beta1FeatureRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**prices** | [**List[V1beta1Price]**](V1beta1Price.md) |  | [optional] 
**credit_amount** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_feature_request_body import V1beta1FeatureRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1FeatureRequestBody from a JSON string
v1beta1_feature_request_body_instance = V1beta1FeatureRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1FeatureRequestBody.to_json()

# convert the object into a dict
v1beta1_feature_request_body_dict = v1beta1_feature_request_body_instance.to_dict()
# create an instance of V1beta1FeatureRequestBody from a dict
v1beta1_feature_request_body_form_dict = v1beta1_feature_request_body.from_dict(v1beta1_feature_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


