# V1beta1Organization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** | The time the organization was created. | [optional] 
**updated_at** | **datetime** | The time the organization was last updated. | [optional] 
**state** | **str** | The state of the organization (enabled or disabled). | [optional] 
**avatar** | **str** | The base64 encoded image string of the organization avatar. Should be less than 2MB. | [optional] 

## Example

```python
from frontier_api.models.v1beta1_organization import V1beta1Organization

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Organization from a JSON string
v1beta1_organization_instance = V1beta1Organization.from_json(json)
# print the JSON string representation of the object
print V1beta1Organization.to_json()

# convert the object into a dict
v1beta1_organization_dict = v1beta1_organization_instance.to_dict()
# create an instance of V1beta1Organization from a dict
v1beta1_organization_form_dict = v1beta1_organization.from_dict(v1beta1_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


