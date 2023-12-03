# V1beta1Subscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**trial_days** | **int** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**canceled_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_subscription import V1beta1Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Subscription from a JSON string
v1beta1_subscription_instance = V1beta1Subscription.from_json(json)
# print the JSON string representation of the object
print V1beta1Subscription.to_json()

# convert the object into a dict
v1beta1_subscription_dict = v1beta1_subscription_instance.to_dict()
# create an instance of V1beta1Subscription from a dict
v1beta1_subscription_form_dict = v1beta1_subscription.from_dict(v1beta1_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


