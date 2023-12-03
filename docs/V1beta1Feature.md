# V1beta1Feature


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**plan_ids** | **List[str]** |  | [optional] 
**state** | **str** |  | [optional] 
**prices** | [**List[V1beta1Price]**](V1beta1Price.md) |  | [optional] 
**credit_amount** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_feature import V1beta1Feature

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Feature from a JSON string
v1beta1_feature_instance = V1beta1Feature.from_json(json)
# print the JSON string representation of the object
print V1beta1Feature.to_json()

# convert the object into a dict
v1beta1_feature_dict = v1beta1_feature_instance.to_dict()
# create an instance of V1beta1Feature from a dict
v1beta1_feature_form_dict = v1beta1_feature.from_dict(v1beta1_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


