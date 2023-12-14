# V1beta1Plan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**features** | [**List[V1beta1Feature]**](V1beta1Feature.md) |  | [optional] 
**interval** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_plan import V1beta1Plan

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Plan from a JSON string
v1beta1_plan_instance = V1beta1Plan.from_json(json)
# print the JSON string representation of the object
print V1beta1Plan.to_json()

# convert the object into a dict
v1beta1_plan_dict = v1beta1_plan_instance.to_dict()
# create an instance of V1beta1Plan from a dict
v1beta1_plan_form_dict = v1beta1_plan.from_dict(v1beta1_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


