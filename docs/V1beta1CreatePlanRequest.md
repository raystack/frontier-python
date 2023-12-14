# V1beta1CreatePlanRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**V1beta1PlanRequestBody**](V1beta1PlanRequestBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_create_plan_request import V1beta1CreatePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CreatePlanRequest from a JSON string
v1beta1_create_plan_request_instance = V1beta1CreatePlanRequest.from_json(json)
# print the JSON string representation of the object
print V1beta1CreatePlanRequest.to_json()

# convert the object into a dict
v1beta1_create_plan_request_dict = v1beta1_create_plan_request_instance.to_dict()
# create an instance of V1beta1CreatePlanRequest from a dict
v1beta1_create_plan_request_form_dict = v1beta1_create_plan_request.from_dict(v1beta1_create_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


