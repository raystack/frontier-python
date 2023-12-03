# V1beta1CheckoutSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**checkout_url** | **str** |  | [optional] 
**success_url** | **str** |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_checkout_session import V1beta1CheckoutSession

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CheckoutSession from a JSON string
v1beta1_checkout_session_instance = V1beta1CheckoutSession.from_json(json)
# print the JSON string representation of the object
print V1beta1CheckoutSession.to_json()

# convert the object into a dict
v1beta1_checkout_session_dict = v1beta1_checkout_session_instance.to_dict()
# create an instance of V1beta1CheckoutSession from a dict
v1beta1_checkout_session_form_dict = v1beta1_checkout_session.from_dict(v1beta1_checkout_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


