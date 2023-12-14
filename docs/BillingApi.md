# frontier_api.BillingApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_billing_account**](BillingApi.md#frontier_service_create_billing_account) | **POST** /v1beta1/organizations/{orgId}/billing | Create billing account
[**frontier_service_delete_billing_account**](BillingApi.md#frontier_service_delete_billing_account) | **DELETE** /v1beta1/organizations/{orgId}/billing/{id} | Delete billing account
[**frontier_service_get_billing_account**](BillingApi.md#frontier_service_get_billing_account) | **GET** /v1beta1/organizations/{orgId}/billing/{id} | Get billing account
[**frontier_service_get_billing_balance**](BillingApi.md#frontier_service_get_billing_balance) | **GET** /v1beta1/organizations/{orgId}/billing/{id}/balance | Get billing balance
[**frontier_service_list_billing_accounts**](BillingApi.md#frontier_service_list_billing_accounts) | **GET** /v1beta1/organizations/{orgId}/billing | List billing accounts
[**frontier_service_update_billing_account**](BillingApi.md#frontier_service_update_billing_account) | **PUT** /v1beta1/organizations/{orgId}/billing/{id} | Update billing account


# **frontier_service_create_billing_account**
> V1beta1CreateBillingAccountResponse frontier_service_create_billing_account(org_id, body)

Create billing account

Create a new billing account for an organization.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_billing_account_request import FrontierServiceCreateBillingAccountRequest
from frontier_api.models.v1beta1_create_billing_account_response import V1beta1CreateBillingAccountResponse
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
    api_instance = frontier_api.BillingApi(api_client)
    org_id = 'org_id_example' # str | ID of the organization to create the billing account for
    body = frontier_api.FrontierServiceCreateBillingAccountRequest() # FrontierServiceCreateBillingAccountRequest | 

    try:
        # Create billing account
        api_response = api_instance.frontier_service_create_billing_account(org_id, body)
        print("The response of BillingApi->frontier_service_create_billing_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->frontier_service_create_billing_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| ID of the organization to create the billing account for | 
 **body** | [**FrontierServiceCreateBillingAccountRequest**](FrontierServiceCreateBillingAccountRequest.md)|  | 

### Return type

[**V1beta1CreateBillingAccountResponse**](V1beta1CreateBillingAccountResponse.md)

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

# **frontier_service_delete_billing_account**
> object frontier_service_delete_billing_account(org_id, id)

Delete billing account

Delete a billing account by ID.

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
    api_instance = frontier_api.BillingApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | ID of the billing account to delete

    try:
        # Delete billing account
        api_response = api_instance.frontier_service_delete_billing_account(org_id, id)
        print("The response of BillingApi->frontier_service_delete_billing_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->frontier_service_delete_billing_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**| ID of the billing account to delete | 

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

# **frontier_service_get_billing_account**
> V1beta1GetBillingAccountResponse frontier_service_get_billing_account(org_id, id)

Get billing account

Get a billing account by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_billing_account_response import V1beta1GetBillingAccountResponse
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
    api_instance = frontier_api.BillingApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | ID of the billing account to get

    try:
        # Get billing account
        api_response = api_instance.frontier_service_get_billing_account(org_id, id)
        print("The response of BillingApi->frontier_service_get_billing_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->frontier_service_get_billing_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**| ID of the billing account to get | 

### Return type

[**V1beta1GetBillingAccountResponse**](V1beta1GetBillingAccountResponse.md)

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

# **frontier_service_get_billing_balance**
> V1beta1GetBillingBalanceResponse frontier_service_get_billing_balance(org_id, id)

Get billing balance

Get the balance of a billing account by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_billing_balance_response import V1beta1GetBillingBalanceResponse
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
    api_instance = frontier_api.BillingApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | ID of the billing account to get the balance for

    try:
        # Get billing balance
        api_response = api_instance.frontier_service_get_billing_balance(org_id, id)
        print("The response of BillingApi->frontier_service_get_billing_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->frontier_service_get_billing_balance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**| ID of the billing account to get the balance for | 

### Return type

[**V1beta1GetBillingBalanceResponse**](V1beta1GetBillingBalanceResponse.md)

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

# **frontier_service_list_billing_accounts**
> V1beta1ListBillingAccountsResponse frontier_service_list_billing_accounts(org_id)

List billing accounts

List billing accounts of an organization.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_billing_accounts_response import V1beta1ListBillingAccountsResponse
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
    api_instance = frontier_api.BillingApi(api_client)
    org_id = 'org_id_example' # str | ID of the organization to list billing accounts for

    try:
        # List billing accounts
        api_response = api_instance.frontier_service_list_billing_accounts(org_id)
        print("The response of BillingApi->frontier_service_list_billing_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->frontier_service_list_billing_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| ID of the organization to list billing accounts for | 

### Return type

[**V1beta1ListBillingAccountsResponse**](V1beta1ListBillingAccountsResponse.md)

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

# **frontier_service_update_billing_account**
> V1beta1UpdateBillingAccountResponse frontier_service_update_billing_account(org_id, id, body)

Update billing account

Update a billing account by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_billing_account_request import FrontierServiceCreateBillingAccountRequest
from frontier_api.models.v1beta1_update_billing_account_response import V1beta1UpdateBillingAccountResponse
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
    api_instance = frontier_api.BillingApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | ID of the billing account to update
    body = frontier_api.FrontierServiceCreateBillingAccountRequest() # FrontierServiceCreateBillingAccountRequest | 

    try:
        # Update billing account
        api_response = api_instance.frontier_service_update_billing_account(org_id, id, body)
        print("The response of BillingApi->frontier_service_update_billing_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->frontier_service_update_billing_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**| ID of the billing account to update | 
 **body** | [**FrontierServiceCreateBillingAccountRequest**](FrontierServiceCreateBillingAccountRequest.md)|  | 

### Return type

[**V1beta1UpdateBillingAccountResponse**](V1beta1UpdateBillingAccountResponse.md)

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

