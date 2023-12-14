# FrontierServiceUpdatePlanRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**V1beta1PlanRequestBody**](V1beta1PlanRequestBody.md) |  | [optional] 

## Example

```python
from frontier_api.models.frontier_service_update_plan_request import FrontierServiceUpdatePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceUpdatePlanRequest from a JSON string
frontier_service_update_plan_request_instance = FrontierServiceUpdatePlanRequest.from_json(json)
# print the JSON string representation of the object
print FrontierServiceUpdatePlanRequest.to_json()

# convert the object into a dict
frontier_service_update_plan_request_dict = frontier_service_update_plan_request_instance.to_dict()
# create an instance of FrontierServiceUpdatePlanRequest from a dict
frontier_service_update_plan_request_form_dict = frontier_service_update_plan_request.from_dict(frontier_service_update_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


