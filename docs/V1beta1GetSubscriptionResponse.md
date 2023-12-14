# V1beta1GetSubscriptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**V1beta1Subscription**](V1beta1Subscription.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_subscription_response import V1beta1GetSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetSubscriptionResponse from a JSON string
v1beta1_get_subscription_response_instance = V1beta1GetSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetSubscriptionResponse.to_json()

# convert the object into a dict
v1beta1_get_subscription_response_dict = v1beta1_get_subscription_response_instance.to_dict()
# create an instance of V1beta1GetSubscriptionResponse from a dict
v1beta1_get_subscription_response_form_dict = v1beta1_get_subscription_response.from_dict(v1beta1_get_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


