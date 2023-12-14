# V1beta1BillingAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**address** | [**BillingAccountAddress**](BillingAccountAddress.md) |  | [optional] 
**provider_id** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_billing_account import V1beta1BillingAccount

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1BillingAccount from a JSON string
v1beta1_billing_account_instance = V1beta1BillingAccount.from_json(json)
# print the JSON string representation of the object
print V1beta1BillingAccount.to_json()

# convert the object into a dict
v1beta1_billing_account_dict = v1beta1_billing_account_instance.to_dict()
# create an instance of V1beta1BillingAccount from a dict
v1beta1_billing_account_form_dict = v1beta1_billing_account.from_dict(v1beta1_billing_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


