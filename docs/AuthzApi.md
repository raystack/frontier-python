# frontier_api.AuthzApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_check_federated_resource_permission**](AuthzApi.md#admin_service_check_federated_resource_permission) | **POST** /v1beta1/admin/check | Check
[**frontier_service_batch_check_permission**](AuthzApi.md#frontier_service_batch_check_permission) | **POST** /v1beta1/batchcheck | Batch check
[**frontier_service_check_resource_permission**](AuthzApi.md#frontier_service_check_resource_permission) | **POST** /v1beta1/check | Check
[**frontier_service_get_jwks**](AuthzApi.md#frontier_service_get_jwks) | **GET** /v1beta1/auth/jwks | Get well known JWKs
[**frontier_service_get_jwks2**](AuthzApi.md#frontier_service_get_jwks2) | **GET** /.well-known/jwks.json | Get well known JWKs


# **admin_service_check_federated_resource_permission**
> V1beta1CheckFederatedResourcePermissionResponse admin_service_check_federated_resource_permission(body)

Check

Returns true if a principal has required permissions to access a resource and false otherwise.<br/> Note the principal can be a user, group or a service account.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_check_federated_resource_permission_request import V1beta1CheckFederatedResourcePermissionRequest
from frontier_api.models.v1beta1_check_federated_resource_permission_response import V1beta1CheckFederatedResourcePermissionResponse
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
    api_instance = frontier_api.AuthzApi(api_client)
    body = frontier_api.V1beta1CheckFederatedResourcePermissionRequest() # V1beta1CheckFederatedResourcePermissionRequest | 

    try:
        # Check
        api_response = api_instance.admin_service_check_federated_resource_permission(body)
        print("The response of AuthzApi->admin_service_check_federated_resource_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->admin_service_check_federated_resource_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CheckFederatedResourcePermissionRequest**](V1beta1CheckFederatedResourcePermissionRequest.md)|  | 

### Return type

[**V1beta1CheckFederatedResourcePermissionResponse**](V1beta1CheckFederatedResourcePermissionResponse.md)

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

# **frontier_service_batch_check_permission**
> V1beta1BatchCheckPermissionResponse frontier_service_batch_check_permission(body)

Batch check

Returns true if a principal has required permissions to access a resource and false otherwise.<br/> Note the principal can be a user or a service account, and Frontier will the credentials from the current logged in principal from the session cookie (if any), or the client id and secret (in case of service users) or the access token (in case of human user accounts).

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_batch_check_permission_request import V1beta1BatchCheckPermissionRequest
from frontier_api.models.v1beta1_batch_check_permission_response import V1beta1BatchCheckPermissionResponse
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
    api_instance = frontier_api.AuthzApi(api_client)
    body = frontier_api.V1beta1BatchCheckPermissionRequest() # V1beta1BatchCheckPermissionRequest | 

    try:
        # Batch check
        api_response = api_instance.frontier_service_batch_check_permission(body)
        print("The response of AuthzApi->frontier_service_batch_check_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->frontier_service_batch_check_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1BatchCheckPermissionRequest**](V1beta1BatchCheckPermissionRequest.md)|  | 

### Return type

[**V1beta1BatchCheckPermissionResponse**](V1beta1BatchCheckPermissionResponse.md)

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

# **frontier_service_check_resource_permission**
> V1beta1CheckResourcePermissionResponse frontier_service_check_resource_permission(body)

Check

Returns true if a principal has required permissions to access a resource and false otherwise.<br/> Note the principal can be a user or a service account. Frontier will extract principal from the current logged in session cookie (if any), or the client id and secret (in case of service users) or the access token.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_check_resource_permission_request import V1beta1CheckResourcePermissionRequest
from frontier_api.models.v1beta1_check_resource_permission_response import V1beta1CheckResourcePermissionResponse
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
    api_instance = frontier_api.AuthzApi(api_client)
    body = frontier_api.V1beta1CheckResourcePermissionRequest() # V1beta1CheckResourcePermissionRequest | 

    try:
        # Check
        api_response = api_instance.frontier_service_check_resource_permission(body)
        print("The response of AuthzApi->frontier_service_check_resource_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->frontier_service_check_resource_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CheckResourcePermissionRequest**](V1beta1CheckResourcePermissionRequest.md)|  | 

### Return type

[**V1beta1CheckResourcePermissionResponse**](V1beta1CheckResourcePermissionResponse.md)

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

# **frontier_service_get_jwks**
> V1beta1GetJWKsResponse frontier_service_get_jwks()

Get well known JWKs

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_jwks_response import V1beta1GetJWKsResponse
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
    api_instance = frontier_api.AuthzApi(api_client)

    try:
        # Get well known JWKs
        api_response = api_instance.frontier_service_get_jwks()
        print("The response of AuthzApi->frontier_service_get_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->frontier_service_get_jwks: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1GetJWKsResponse**](V1beta1GetJWKsResponse.md)

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

# **frontier_service_get_jwks2**
> V1beta1GetJWKsResponse frontier_service_get_jwks2()

Get well known JWKs

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_jwks_response import V1beta1GetJWKsResponse
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
    api_instance = frontier_api.AuthzApi(api_client)

    try:
        # Get well known JWKs
        api_response = api_instance.frontier_service_get_jwks2()
        print("The response of AuthzApi->frontier_service_get_jwks2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->frontier_service_get_jwks2: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1GetJWKsResponse**](V1beta1GetJWKsResponse.md)

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

