# V1beta1RelationRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**relation** | **str** |  | [optional] 
**subject_sub_relation** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_relation_request_body import V1beta1RelationRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1RelationRequestBody from a JSON string
v1beta1_relation_request_body_instance = V1beta1RelationRequestBody.from_json(json)
# print the JSON string representation of the object
print V1beta1RelationRequestBody.to_json()

# convert the object into a dict
v1beta1_relation_request_body_dict = v1beta1_relation_request_body_instance.to_dict()
# create an instance of V1beta1RelationRequestBody from a dict
v1beta1_relation_request_body_form_dict = v1beta1_relation_request_body.from_dict(v1beta1_relation_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


