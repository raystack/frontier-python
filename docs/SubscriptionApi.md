# frontier_api.SubscriptionApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_cancel_subscription**](SubscriptionApi.md#frontier_service_cancel_subscription) | **POST** /v1beta1/organizations/{orgId}/billing/{billingId}/subscriptions/{id}/cancel | Cancel subscription
[**frontier_service_get_subscription**](SubscriptionApi.md#frontier_service_get_subscription) | **GET** /v1beta1/organizations/{orgId}/billing/{billingId}/subscriptions/{id} | Get subscription
[**frontier_service_list_subscriptions**](SubscriptionApi.md#frontier_service_list_subscriptions) | **GET** /v1beta1/organizations/{orgId}/billing/{billingId}/subscriptions | List subscriptions
[**frontier_service_update_subscription**](SubscriptionApi.md#frontier_service_update_subscription) | **PUT** /v1beta1/organizations/{orgId}/billing/{billingId}/subscriptions/{id} | Update subscription


# **frontier_service_cancel_subscription**
> object frontier_service_cancel_subscription(org_id, billing_id, id)

Cancel subscription

Cancel a subscription by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
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
    api_instance = frontier_api.SubscriptionApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to update the subscription for
    id = 'id_example' # str | ID of the subscription to cancel

    try:
        # Cancel subscription
        api_response = api_instance.frontier_service_cancel_subscription(org_id, billing_id, id)
        print("The response of SubscriptionApi->frontier_service_cancel_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->frontier_service_cancel_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to update the subscription for | 
 **id** | **str**| ID of the subscription to cancel | 

### Return type

**object**

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

# **frontier_service_get_subscription**
> V1beta1GetSubscriptionResponse frontier_service_get_subscription(org_id, billing_id, id)

Get subscription

Get a subscription by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_subscription_response import V1beta1GetSubscriptionResponse
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
    api_instance = frontier_api.SubscriptionApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to get the subscription for
    id = 'id_example' # str | ID of the subscription to get

    try:
        # Get subscription
        api_response = api_instance.frontier_service_get_subscription(org_id, billing_id, id)
        print("The response of SubscriptionApi->frontier_service_get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->frontier_service_get_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to get the subscription for | 
 **id** | **str**| ID of the subscription to get | 

### Return type

[**V1beta1GetSubscriptionResponse**](V1beta1GetSubscriptionResponse.md)

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

# **frontier_service_list_subscriptions**
> V1beta1ListSubscriptionsResponse frontier_service_list_subscriptions(org_id, billing_id)

List subscriptions

List subscriptions of a billing account.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_subscriptions_response import V1beta1ListSubscriptionsResponse
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
    api_instance = frontier_api.SubscriptionApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to list subscriptions for

    try:
        # List subscriptions
        api_response = api_instance.frontier_service_list_subscriptions(org_id, billing_id)
        print("The response of SubscriptionApi->frontier_service_list_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->frontier_service_list_subscriptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to list subscriptions for | 

### Return type

[**V1beta1ListSubscriptionsResponse**](V1beta1ListSubscriptionsResponse.md)

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

# **frontier_service_update_subscription**
> V1beta1UpdateSubscriptionResponse frontier_service_update_subscription(org_id, billing_id, id, body)

Update subscription

Update a subscription by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_update_subscription_request import FrontierServiceUpdateSubscriptionRequest
from frontier_api.models.v1beta1_update_subscription_response import V1beta1UpdateSubscriptionResponse
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
    api_instance = frontier_api.SubscriptionApi(api_client)
    org_id = 'org_id_example' # str | 
    billing_id = 'billing_id_example' # str | ID of the billing account to update the subscription for
    id = 'id_example' # str | ID of the subscription to update
    body = frontier_api.FrontierServiceUpdateSubscriptionRequest() # FrontierServiceUpdateSubscriptionRequest | 

    try:
        # Update subscription
        api_response = api_instance.frontier_service_update_subscription(org_id, billing_id, id, body)
        print("The response of SubscriptionApi->frontier_service_update_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->frontier_service_update_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **billing_id** | **str**| ID of the billing account to update the subscription for | 
 **id** | **str**| ID of the subscription to update | 
 **body** | [**FrontierServiceUpdateSubscriptionRequest**](FrontierServiceUpdateSubscriptionRequest.md)|  | 

### Return type

[**V1beta1UpdateSubscriptionResponse**](V1beta1UpdateSubscriptionResponse.md)

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

