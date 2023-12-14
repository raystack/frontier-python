# V1beta1ListSubscriptionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[V1beta1Subscription]**](V1beta1Subscription.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_subscriptions_response import V1beta1ListSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListSubscriptionsResponse from a JSON string
v1beta1_list_subscriptions_response_instance = V1beta1ListSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListSubscriptionsResponse.to_json()

# convert the object into a dict
v1beta1_list_subscriptions_response_dict = v1beta1_list_subscriptions_response_instance.to_dict()
# create an instance of V1beta1ListSubscriptionsResponse from a dict
v1beta1_list_subscriptions_response_form_dict = v1beta1_list_subscriptions_response.from_dict(v1beta1_list_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


