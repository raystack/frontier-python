# frontier_api.UsageApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_billing_usage**](UsageApi.md#frontier_service_create_billing_usage) | **POST** /v1beta1/organizations/{orgId}/billing/{billingId}/usages | Create billing usage


# **frontier_service_create_billing_usage**
> object frontier_service_create_billing_usage(org_id, billing_id, body)

Create billing usage

Report a new billing usage for a billing account.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_billing_usage_request import FrontierServiceCreateBillingUsageRequest
from frontier_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:7400
# See configuration.py for a list of all supported configuration parameters.
configuration = frontier_api.Configuration(
    host = "http://127.0.0.1:7400"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = frontier_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with frontier_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontier_api.UsageApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to update the subscription for
    body = frontier_api.FrontierServiceCreateBillingUsageRequest() # FrontierServiceCreateBillingUsageRequest | 

    try:
        # Create billing usage
        api_response = api_instance.frontier_service_create_billing_usage(org_id, billing_id, body)
        print("The response of UsageApi->frontier_service_create_billing_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->frontier_service_create_billing_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to update the subscription for | 
 **body** | [**FrontierServiceCreateBillingUsageRequest**](FrontierServiceCreateBillingUsageRequest.md)|  | 

### Return type

**object**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Bad Request - The request was malformed or contained invalid parameters. |  -  |
**401** | Unauthorized - Authentication is required |  -  |
**403** | Forbidden - User does not have permission to access the resource |  -  |
**404** | Not Found - The requested resource was not found |  -  |
**500** | Internal Server Error. Returned when theres is something wrong with Frontier server. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

