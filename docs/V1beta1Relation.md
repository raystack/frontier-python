# V1beta1Relation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** | The time the relation was created. | [optional] 
**updated_at** | **datetime** | The time the relation was last updated. | [optional] 
**subject_sub_relation** | **str** |  | [optional] 
**relation** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_relation import V1beta1Relation

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Relation from a JSON string
v1beta1_relation_instance = V1beta1Relation.from_json(json)
# print the JSON string representation of the object
print V1beta1Relation.to_json()

# convert the object into a dict
v1beta1_relation_dict = v1beta1_relation_instance.to_dict()
# create an instance of V1beta1Relation from a dict
v1beta1_relation_form_dict = v1beta1_relation.from_dict(v1beta1_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


