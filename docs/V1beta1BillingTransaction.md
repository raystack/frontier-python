# V1beta1BillingTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_billing_transaction import V1beta1BillingTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1BillingTransaction from a JSON string
v1beta1_billing_transaction_instance = V1beta1BillingTransaction.from_json(json)
# print the JSON string representation of the object
print V1beta1BillingTransaction.to_json()

# convert the object into a dict
v1beta1_billing_transaction_dict = v1beta1_billing_transaction_instance.to_dict()
# create an instance of V1beta1BillingTransaction from a dict
v1beta1_billing_transaction_form_dict = v1beta1_billing_transaction.from_dict(v1beta1_billing_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


