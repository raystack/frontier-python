# FrontierServiceAuthenticate2Request


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_onstart** | **bool** | If set to true, location header will be set for redirect to start auth flow | [optional] 
**return_to** | **str** | URL to redirect after successful authentication.&lt;br/&gt; *Example:*&#x60;\&quot;https://frontier.example.com\&quot;&#x60; | [optional] 
**email** | **str** | Email of the user to authenticate. Used for magic links.&lt;br/&gt; *Example:*&#x60;example@acme.org&#x60; | [optional] 
**callback_url** | **str** | Host which should handle the call to finish authentication flow, for most cases it could be host of frontier but in case of proxies, this will be proxy public endpoint.&lt;br/&gt; *Example:*&#x60;https://frontier.example.com/v1beta1/auth/callback&#x60; | [optional] 

## Example

```python
from frontier_api.models.frontier_service_authenticate2_request import FrontierServiceAuthenticate2Request

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierServiceAuthenticate2Request from a JSON string
frontier_service_authenticate2_request_instance = FrontierServiceAuthenticate2Request.from_json(json)
# print the JSON string representation of the object
print FrontierServiceAuthenticate2Request.to_json()

# convert the object into a dict
frontier_service_authenticate2_request_dict = frontier_service_authenticate2_request_instance.to_dict()
# create an instance of FrontierServiceAuthenticate2Request from a dict
frontier_service_authenticate2_request_form_dict = frontier_service_authenticate2_request.from_dict(frontier_service_authenticate2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


