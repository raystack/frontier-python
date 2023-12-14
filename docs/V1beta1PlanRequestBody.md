# V1beta1PlanRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**features** | [**List[V1beta1Feature]**](V1beta1Feature.md) |  | [optional] 
**interval** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_plan_request_body import V1beta1PlanRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PlanRequestBody from a JSON string
v1beta1_plan_request_body_instance = V1beta1PlanRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1PlanRequestBody.to_json()

# convert the object into a dict
v1beta1_plan_request_body_dict = v1beta1_plan_request_body_instance.to_dict()
# create an instance of V1beta1PlanRequestBody from a dict
v1beta1_plan_request_body_form_dict = v1beta1_plan_request_body.from_dict(v1beta1_plan_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


