# V1beta1Domain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The domain id | [optional] 
**name** | **str** | The domain name | [optional] 
**org_id** | **str** | The organization id | [optional] 
**token** | **str** | The dns TXT record token to verify the domain | [optional] 
**state** | **str** | The domain state either pending or verified | [optional] 
**created_at** | **datetime** | The time the domain whitelist request was created | [optional] 
**updated_at** | **datetime** | The time the org domain was updated | [optional] 

## Example

```python
from frontier_api.models.v1beta1_domain import V1beta1Domain

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Domain from a JSON string
v1beta1_domain_instance = V1beta1Domain.from_json(json)
# print the JSON string representation of the object
print V1beta1Domain.to_json()

# convert the object into a dict
v1beta1_domain_dict = v1beta1_domain_instance.to_dict()
# create an instance of V1beta1Domain from a dict
v1beta1_domain_form_dict = v1beta1_domain.from_dict(v1beta1_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


