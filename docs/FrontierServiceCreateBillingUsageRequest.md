# FrontierServiceCreateBillingUsageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usages** | [**List[V1beta1Usage]**](V1beta1Usage.md) |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_create_billing_usage_request import FrontierServiceCreateBillingUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceCreateBillingUsageRequest from a JSON string
frontier_service_create_billing_usage_request_instance = FrontierServiceCreateBillingUsageRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceCreateBillingUsageRequest.to_json()

# convert the object into a dict
frontier_service_create_billing_usage_request_dict = frontier_service_create_billing_usage_request_instance.to_dict()
# create an instance of FrontierServiceCreateBillingUsageRequest from a dict
frontier_service_create_billing_usage_request_form_dict = frontier_service_create_billing_usage_request.from_dict(frontier_service_create_billing_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


