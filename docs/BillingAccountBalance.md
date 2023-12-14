# BillingAccountBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.billing_account_balance import BillingAccountBalance

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAccountBalance from a JSON string
billing_account_balance_instance = BillingAccountBalance.from_json(json)
# print the JSON string representation of the object
print BillingAccountBalance.to_json()

# convert the object into a dict
billing_account_balance_dict = billing_account_balance_instance.to_dict()
# create an instance of BillingAccountBalance from a dict
billing_account_balance_form_dict = billing_account_balance.from_dict(billing_account_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


