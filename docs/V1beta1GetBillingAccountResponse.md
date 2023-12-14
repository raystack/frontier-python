# V1beta1GetBillingAccountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_account** | [**V1beta1BillingAccount**](V1beta1BillingAccount.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_billing_account_response import V1beta1GetBillingAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetBillingAccountResponse from a JSON string
v1beta1_get_billing_account_response_instance = V1beta1GetBillingAccountResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetBillingAccountResponse.to_json()

# convert the object into a dict
v1beta1_get_billing_account_response_dict = v1beta1_get_billing_account_response_instance.to_dict()
# create an instance of V1beta1GetBillingAccountResponse from a dict
v1beta1_get_billing_account_response_form_dict = v1beta1_get_billing_account_response.from_dict(v1beta1_get_billing_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


