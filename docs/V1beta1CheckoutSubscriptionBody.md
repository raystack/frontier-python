# V1beta1CheckoutSubscriptionBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** |  | [optional] 
**trail_days** | **int** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_checkout_subscription_body import V1beta1CheckoutSubscriptionBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CheckoutSubscriptionBody from a JSON string
v1beta1_checkout_subscription_body_instance = V1beta1CheckoutSubscriptionBody.from_json(json)
# print the JSON string representation of the object
print V1beta1CheckoutSubscriptionBody.to_json()

# convert the object into a dict
v1beta1_checkout_subscription_body_dict = v1beta1_checkout_subscription_body_instance.to_dict()
# create an instance of V1beta1CheckoutSubscriptionBody from a dict
v1beta1_checkout_subscription_body_form_dict = v1beta1_checkout_subscription_body.from_dict(v1beta1_checkout_subscription_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


