# frontier_api.CheckoutApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_delegated_checkout**](CheckoutApi.md#admin_service_delegated_checkout) | **POST** /v1beta1/admin/organizations/{orgId}/billing/{billingId}/checkouts | Checkout a feature or subscription
[**frontier_service_create_checkout**](CheckoutApi.md#frontier_service_create_checkout) | **POST** /v1beta1/organizations/{orgId}/billing/{billingId}/checkouts | Checkout a feature or subscription
[**frontier_service_list_checkouts**](CheckoutApi.md#frontier_service_list_checkouts) | **GET** /v1beta1/organizations/{orgId}/billing/{billingId}/checkouts | List checkouts


# **admin_service_delegated_checkout**
> V1beta1DelegatedCheckoutResponse admin_service_delegated_checkout(org_id, billing_id, body)

Checkout a feature or subscription

Checkout a feature to buy it one time or start a subscription plan on a billing account manually. It bypasses billing engine.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.admin_service_delegated_checkout_request import AdminServiceDelegatedCheckoutRequest
from frontier_api.models.v1beta1_delegated_checkout_response import V1beta1DelegatedCheckoutResponse
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
    api_instance = frontier_api.CheckoutApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to update the subscription for
    body = frontier_api.AdminServiceDelegatedCheckoutRequest() # AdminServiceDelegatedCheckoutRequest | 

    try:
        # Checkout a feature or subscription
        api_response = api_instance.admin_service_delegated_checkout(org_id, billing_id, body)
        print("The response of CheckoutApi->admin_service_delegated_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->admin_service_delegated_checkout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to update the subscription for | 
 **body** | [**AdminServiceDelegatedCheckoutRequest**](AdminServiceDelegatedCheckoutRequest.md)|  | 

### Return type

[**V1beta1DelegatedCheckoutResponse**](V1beta1DelegatedCheckoutResponse.md)

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

# **frontier_service_create_checkout**
> V1beta1CreateCheckoutResponse frontier_service_create_checkout(org_id, billing_id, body)

Checkout a feature or subscription

Checkout a feature to buy it one time or start a subscription plan on a billing account.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_checkout_request import FrontierServiceCreateCheckoutRequest
from frontier_api.models.v1beta1_create_checkout_response import V1beta1CreateCheckoutResponse
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
    api_instance = frontier_api.CheckoutApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to update the subscription for
    body = frontier_api.FrontierServiceCreateCheckoutRequest() # FrontierServiceCreateCheckoutRequest | 

    try:
        # Checkout a feature or subscription
        api_response = api_instance.frontier_service_create_checkout(org_id, billing_id, body)
        print("The response of CheckoutApi->frontier_service_create_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->frontier_service_create_checkout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to update the subscription for | 
 **body** | [**FrontierServiceCreateCheckoutRequest**](FrontierServiceCreateCheckoutRequest.md)|  | 

### Return type

[**V1beta1CreateCheckoutResponse**](V1beta1CreateCheckoutResponse.md)

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

# **frontier_service_list_checkouts**
> V1beta1ListCheckoutsResponse frontier_service_list_checkouts(org_id, billing_id)

List checkouts

List all checkouts of a billing account.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_checkouts_response import V1beta1ListCheckoutsResponse
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
    api_instance = frontier_api.CheckoutApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to update the subscription for

    try:
        # List checkouts
        api_response = api_instance.frontier_service_list_checkouts(org_id, billing_id)
        print("The response of CheckoutApi->frontier_service_list_checkouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->frontier_service_list_checkouts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to update the subscription for | 

### Return type

[**V1beta1ListCheckoutsResponse**](V1beta1ListCheckoutsResponse.md)

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

