# V1beta1GetPlanResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**V1beta1Plan**](V1beta1Plan.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_get_plan_response import V1beta1GetPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GetPlanResponse from a JSON string
v1beta1_get_plan_response_instance = V1beta1GetPlanResponse.from_json(json)
# print the JSON string representation of the object
print V1beta1GetPlanResponse.to_json()

# convert the object into a dict
v1beta1_get_plan_response_dict = v1beta1_get_plan_response_instance.to_dict()
# create an instance of V1beta1GetPlanResponse from a dict
v1beta1_get_plan_response_form_dict = v1beta1_get_plan_response.from_dict(v1beta1_get_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

