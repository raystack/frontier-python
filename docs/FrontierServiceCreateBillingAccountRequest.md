# FrontierServiceCreateBillingAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**V1beta1BillingAccountRequestBody**](V1beta1BillingAccountRequestBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_create_billing_account_request import FrontierServiceCreateBillingAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceCreateBillingAccountRequest from a JSON string
frontier_service_create_billing_account_request_instance = FrontierServiceCreateBillingAccountRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceCreateBillingAccountRequest.to_json()

# convert the object into a dict
frontier_service_create_billing_account_request_dict = frontier_service_create_billing_account_request_instance.to_dict()
# create an instance of FrontierServiceCreateBillingAccountRequest from a dict
frontier_service_create_billing_account_request_form_dict = frontier_service_create_billing_account_request.from_dict(frontier_service_create_billing_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


