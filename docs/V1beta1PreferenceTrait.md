# V1beta1PreferenceTrait


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**long_description** | **str** |  | [optional] 
**heading** | **str** |  | [optional] 
**sub_heading** | **str** |  | [optional] 
**breadcrumb** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**input_hints** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**textarea** | **str** |  | [optional] 
**select** | **str** |  | [optional] 
**combobox** | **str** |  | [optional] 
**checkbox** | **str** |  | [optional] 
**multiselect** | **str** |  | [optional] 
**number** | **str** |  | [optional] 

## Example

```python
from frontier_api.models.v1beta1_preference_trait import V1beta1PreferenceTrait

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PreferenceTrait from a JSON string
v1beta1_preference_trait_instance = V1beta1PreferenceTrait.from_json(json)
# print the JSON string representation of the object
print V1beta1PreferenceTrait.to_json()

# convert the object into a dict
v1beta1_preference_trait_dict = v1beta1_preference_trait_instance.to_dict()
# create an instance of V1beta1PreferenceTrait from a dict
v1beta1_preference_trait_form_dict = v1beta1_preference_trait.from_dict(v1beta1_preference_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


