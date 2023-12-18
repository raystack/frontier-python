# AdminServiceDelegatedCheckoutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_body** | [**V1beta1CheckoutSubscriptionBody**](V1beta1CheckoutSubscriptionBody.md) |  | [optional] 
**feature_body** | [**V1beta1CheckoutFeatureBody**](V1beta1CheckoutFeatureBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.admin_service_delegated_checkout_request import AdminServiceDelegatedCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminServiceDelegatedCheckoutRequest from a JSON string
admin_service_delegated_checkout_request_instance = AdminServiceDelegatedCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print AdminServiceDelegatedCheckoutRequest.to_json()

# convert the object into a dict
admin_service_delegated_checkout_request_dict = admin_service_delegated_checkout_request_instance.to_dict()
# create an instance of AdminServiceDelegatedCheckoutRequest from a dict
admin_service_delegated_checkout_request_form_dict = admin_service_delegated_checkout_request.from_dict(admin_service_delegated_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


