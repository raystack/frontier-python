# V1beta1Price


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**feature_id** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**usage_type** | **str** |  | [optional] 
**billing_scheme** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**metered_aggregate** | **str** |  | [optional] 
**tier_mode** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_price import V1beta1Price

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Price from a JSON string
v1beta1_price_instance = V1beta1Price.from_json(json)
# print the JSON string representation of the object
print V1beta1Price.to_json()

# convert the object into a dict
v1beta1_price_dict = v1beta1_price_instance.to_dict()
# create an instance of V1beta1Price from a dict
v1beta1_price_form_dict = v1beta1_price.from_dict(v1beta1_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


