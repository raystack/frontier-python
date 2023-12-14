# frontier_api.PermissionApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_create_permission**](PermissionApi.md#admin_service_create_permission) | **POST** /v1beta1/permissions | Create platform permission
[**admin_service_delete_permission**](PermissionApi.md#admin_service_delete_permission) | **DELETE** /v1beta1/permissions/{id} | Delete platform permission
[**admin_service_update_permission**](PermissionApi.md#admin_service_update_permission) | **PUT** /v1beta1/permissions/{id} | Update platform permission
[**frontier_service_get_permission**](PermissionApi.md#frontier_service_get_permission) | **GET** /v1beta1/permissions/{id} | Get permission
[**frontier_service_list_permissions**](PermissionApi.md#frontier_service_list_permissions) | **GET** /v1beta1/permissions | Get all permissions


# **admin_service_create_permission**
> V1beta1CreatePermissionResponse admin_service_create_permission(body)

Create platform permission

Creates a permission. It can be used to grant permissions to all the resources in a Frontier instance.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_permission_request import V1beta1CreatePermissionRequest
from frontier_api.models.v1beta1_create_permission_response import V1beta1CreatePermissionResponse
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
    api_instance = frontier_api.PermissionApi(api_client)
    body = frontier_api.V1beta1CreatePermissionRequest() # V1beta1CreatePermissionRequest | 

    try:
        # Create platform permission
        api_response = api_instance.admin_service_create_permission(body)
        print("The response of PermissionApi->admin_service_create_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->admin_service_create_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CreatePermissionRequest**](V1beta1CreatePermissionRequest.md)|  | 

### Return type

[**V1beta1CreatePermissionResponse**](V1beta1CreatePermissionResponse.md)

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

# **admin_service_delete_permission**
> object admin_service_delete_permission(id)

Delete platform permission

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
    api_instance = frontier_api.PermissionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete platform permission
        api_response = api_instance.admin_service_delete_permission(id)
        print("The response of PermissionApi->admin_service_delete_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->admin_service_delete_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **admin_service_update_permission**
> V1beta1UpdatePermissionResponse admin_service_update_permission(id, body)

Update platform permission

Updates a permission by ID. It can be used to grant permissions to all the resources in a Frontier instance.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_permission_request_body import V1beta1PermissionRequestBody
from frontier_api.models.v1beta1_update_permission_response import V1beta1UpdatePermissionResponse
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
    api_instance = frontier_api.PermissionApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.V1beta1PermissionRequestBody() # V1beta1PermissionRequestBody | 

    try:
        # Update platform permission
        api_response = api_instance.admin_service_update_permission(id, body)
        print("The response of PermissionApi->admin_service_update_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->admin_service_update_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**V1beta1PermissionRequestBody**](V1beta1PermissionRequestBody.md)|  | 

### Return type

[**V1beta1UpdatePermissionResponse**](V1beta1UpdatePermissionResponse.md)

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

# **frontier_service_get_permission**
> V1beta1GetPermissionResponse frontier_service_get_permission(id)

Get permission

Returns a permission by ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_permission_response import V1beta1GetPermissionResponse
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
    api_instance = frontier_api.PermissionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get permission
        api_response = api_instance.frontier_service_get_permission(id)
        print("The response of PermissionApi->frontier_service_get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->frontier_service_get_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1GetPermissionResponse**](V1beta1GetPermissionResponse.md)

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

# **frontier_service_list_permissions**
> V1beta1ListPermissionsResponse frontier_service_list_permissions()

Get all permissions

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_permissions_response import V1beta1ListPermissionsResponse
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
    api_instance = frontier_api.PermissionApi(api_client)

    try:
        # Get all permissions
        api_response = api_instance.frontier_service_list_permissions()
        print("The response of PermissionApi->frontier_service_list_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->frontier_service_list_permissions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListPermissionsResponse**](V1beta1ListPermissionsResponse.md)

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

