# frontier_api.TransactionApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_list_billing_transactions**](TransactionApi.md#frontier_service_list_billing_transactions) | **GET** /v1beta1/billing/{billingId}/transactions | List billing transactions


# **frontier_service_list_billing_transactions**
> V1beta1ListBillingTransactionsResponse frontier_service_list_billing_transactions(billing_id, org_id=org_id, since=since)

List billing transactions

List all transactions of a billing account.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_billing_transactions_response import V1beta1ListBillingTransactionsResponse
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
    api_instance = frontier_api.TransactionApi(api_client)
    billing_id = 'billing_id_example' # str | ID of the billing account to update the subscription for
    org_id = 'org_id_example' # str |  (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # List billing transactions
        api_response = api_instance.frontier_service_list_billing_transactions(billing_id, org_id=org_id, since=since)
        print("The response of TransactionApi->frontier_service_list_billing_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->frontier_service_list_billing_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_id** | **str**| ID of the billing account to update the subscription for | 
 **org_id** | **str**|  | [optional] 
 **since** | **datetime**|  | [optional] 

### Return type

[**V1beta1ListBillingTransactionsResponse**](V1beta1ListBillingTransactionsResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
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

