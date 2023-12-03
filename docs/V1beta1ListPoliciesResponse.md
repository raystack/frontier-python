# V1beta1ListPoliciesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[V1beta1Policy]**](V1beta1Policy.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_list_policies_response import V1beta1ListPoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ListPoliciesResponse from a JSON string
v1beta1_list_policies_response_instance = V1beta1ListPoliciesResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1ListPoliciesResponse.to_json()

# convert the object into a dict
v1beta1_list_policies_response_dict = v1beta1_list_policies_response_instance.to_dict()
# create an instance of V1beta1ListPoliciesResponse from a dict
v1beta1_list_policies_response_form_dict = v1beta1_list_policies_response.from_dict(v1beta1_list_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


