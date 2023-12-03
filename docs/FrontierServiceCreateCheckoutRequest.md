# FrontierServiceCreateCheckoutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_url** | **str** |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**subscription_body** | [**V1beta1CheckoutSubscriptionBody**](V1beta1CheckoutSubscriptionBody.md) |  | [optional] 
**feature_body** | [**V1beta1CheckoutFeatureBody**](V1beta1CheckoutFeatureBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_create_checkout_request import FrontierServiceCreateCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceCreateCheckoutRequest from a JSON string
frontier_service_create_checkout_request_instance = FrontierServiceCreateCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceCreateCheckoutRequest.to_json()

# convert the object into a dict
frontier_service_create_checkout_request_dict = frontier_service_create_checkout_request_instance.to_dict()
# create an instance of FrontierServiceCreateCheckoutRequest from a dict
frontier_service_create_checkout_request_form_dict = frontier_service_create_checkout_request.from_dict(frontier_service_create_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


