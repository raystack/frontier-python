# BillingAccountAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** |  | [optional] 
**line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.billing_account_address import BillingAccountAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAccountAddress from a JSON string
billing_account_address_instance = BillingAccountAddress.from_json(json)
# print the JSON string representation of the object
print BillingAccountAddress.to_json()

# convert the object into a dict
billing_account_address_dict = billing_account_address_instance.to_dict()
# create an instance of BillingAccountAddress from a dict
billing_account_address_form_dict = billing_account_address.from_dict(billing_account_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


