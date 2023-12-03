# frontier_api.ServiceUserApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_service_user**](ServiceUserApi.md#frontier_service_create_service_user) | **POST** /v1beta1/serviceusers | Create service user
[**frontier_service_create_service_user_key**](ServiceUserApi.md#frontier_service_create_service_user_key) | **POST** /v1beta1/serviceusers/{id}/keys | Create service user key
[**frontier_service_create_service_user_secret**](ServiceUserApi.md#frontier_service_create_service_user_secret) | **POST** /v1beta1/serviceusers/{id}/secrets | Create service user secret
[**frontier_service_delete_service_user**](ServiceUserApi.md#frontier_service_delete_service_user) | **DELETE** /v1beta1/serviceusers/{id} | Delete service user
[**frontier_service_delete_service_user_key**](ServiceUserApi.md#frontier_service_delete_service_user_key) | **DELETE** /v1beta1/serviceusers/{id}/keys/{keyId} | Delete service user key
[**frontier_service_delete_service_user_secret**](ServiceUserApi.md#frontier_service_delete_service_user_secret) | **DELETE** /v1beta1/serviceusers/{id}/secrets/{secretId} | Delete service user secret
[**frontier_service_get_service_user**](ServiceUserApi.md#frontier_service_get_service_user) | **GET** /v1beta1/serviceusers/{id} | Get service user
[**frontier_service_get_service_user_key**](ServiceUserApi.md#frontier_service_get_service_user_key) | **GET** /v1beta1/serviceusers/{id}/keys/{keyId} | Get service user key
[**frontier_service_list_service_user_keys**](ServiceUserApi.md#frontier_service_list_service_user_keys) | **GET** /v1beta1/serviceusers/{id}/keys | List service user keys
[**frontier_service_list_service_user_secrets**](ServiceUserApi.md#frontier_service_list_service_user_secrets) | **GET** /v1beta1/serviceusers/{id}/secrets | List service user secrets
[**frontier_service_list_service_users**](ServiceUserApi.md#frontier_service_list_service_users) | **GET** /v1beta1/serviceusers | List org service users


# **frontier_service_create_service_user**
> V1beta1CreateServiceUserResponse frontier_service_create_service_user(body)

Create service user

Create a service user.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_service_user_request import V1beta1CreateServiceUserRequest
from frontier_api.models.v1beta1_create_service_user_response import V1beta1CreateServiceUserResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    body = frontier_api.V1beta1CreateServiceUserRequest() # V1beta1CreateServiceUserRequest | 

    try:
        # Create service user
        api_response = api_instance.frontier_service_create_service_user(body)
        print("The response of ServiceUserApi->frontier_service_create_service_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_create_service_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CreateServiceUserRequest**](V1beta1CreateServiceUserRequest.md)|  | 

### Return type

[**V1beta1CreateServiceUserResponse**](V1beta1CreateServiceUserResponse.md)

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

# **frontier_service_create_service_user_key**
> V1beta1CreateServiceUserKeyResponse frontier_service_create_service_user_key(id, body)

Create service user key

Generate a service user key and return it, the private key part of the response will not be persisted and should be kept securely by client.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_service_user_key_request import FrontierServiceCreateServiceUserKeyRequest
from frontier_api.models.v1beta1_create_service_user_key_response import V1beta1CreateServiceUserKeyResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to create a key for.
    body = frontier_api.FrontierServiceCreateServiceUserKeyRequest() # FrontierServiceCreateServiceUserKeyRequest | 

    try:
        # Create service user key
        api_response = api_instance.frontier_service_create_service_user_key(id, body)
        print("The response of ServiceUserApi->frontier_service_create_service_user_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_create_service_user_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to create a key for. | 
 **body** | [**FrontierServiceCreateServiceUserKeyRequest**](FrontierServiceCreateServiceUserKeyRequest.md)|  | 

### Return type

[**V1beta1CreateServiceUserKeyResponse**](V1beta1CreateServiceUserKeyResponse.md)

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

# **frontier_service_create_service_user_secret**
> V1beta1CreateServiceUserSecretResponse frontier_service_create_service_user_secret(id, body)

Create service user secret

Generate a service user secret and return it. The secret value will not be persisted and should be securely stored by client.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_service_user_key_request import FrontierServiceCreateServiceUserKeyRequest
from frontier_api.models.v1beta1_create_service_user_secret_response import V1beta1CreateServiceUserSecretResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to create a key for.
    body = frontier_api.FrontierServiceCreateServiceUserKeyRequest() # FrontierServiceCreateServiceUserKeyRequest | 

    try:
        # Create service user secret
        api_response = api_instance.frontier_service_create_service_user_secret(id, body)
        print("The response of ServiceUserApi->frontier_service_create_service_user_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_create_service_user_secret: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to create a key for. | 
 **body** | [**FrontierServiceCreateServiceUserKeyRequest**](FrontierServiceCreateServiceUserKeyRequest.md)|  | 

### Return type

[**V1beta1CreateServiceUserSecretResponse**](V1beta1CreateServiceUserSecretResponse.md)

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

# **frontier_service_delete_service_user**
> object frontier_service_delete_service_user(id, org_id=org_id)

Delete service user

Delete a service user permanently and all of its relations (keys, organizations, roles, etc)

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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to delete.
    org_id = 'org_id_example' # str |  (optional)

    try:
        # Delete service user
        api_response = api_instance.frontier_service_delete_service_user(id, org_id=org_id)
        print("The response of ServiceUserApi->frontier_service_delete_service_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_delete_service_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to delete. | 
 **org_id** | **str**|  | [optional] 

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

# **frontier_service_delete_service_user_key**
> object frontier_service_delete_service_user_key(id, key_id)

Delete service user key

Delete a service user key permanently.

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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to delete a key for.
    key_id = 'key_id_example' # str | The unique ID of the key to delete.

    try:
        # Delete service user key
        api_response = api_instance.frontier_service_delete_service_user_key(id, key_id)
        print("The response of ServiceUserApi->frontier_service_delete_service_user_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_delete_service_user_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to delete a key for. | 
 **key_id** | **str**| The unique ID of the key to delete. | 

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

# **frontier_service_delete_service_user_secret**
> object frontier_service_delete_service_user_secret(id, secret_id)

Delete service user secret

Delete a service user secret credential.

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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to delete a secret for.
    secret_id = 'secret_id_example' # str | The unique ID of the secret to delete.

    try:
        # Delete service user secret
        api_response = api_instance.frontier_service_delete_service_user_secret(id, secret_id)
        print("The response of ServiceUserApi->frontier_service_delete_service_user_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_delete_service_user_secret: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to delete a secret for. | 
 **secret_id** | **str**| The unique ID of the secret to delete. | 

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

# **frontier_service_get_service_user**
> V1beta1GetServiceUserResponse frontier_service_get_service_user(id)

Get service user

Get service user details by its id.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_service_user_response import V1beta1GetServiceUserResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to get.

    try:
        # Get service user
        api_response = api_instance.frontier_service_get_service_user(id)
        print("The response of ServiceUserApi->frontier_service_get_service_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_get_service_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to get. | 

### Return type

[**V1beta1GetServiceUserResponse**](V1beta1GetServiceUserResponse.md)

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

# **frontier_service_get_service_user_key**
> V1beta1GetServiceUserKeyResponse frontier_service_get_service_user_key(id, key_id)

Get service user key

Get a service user public RSA JWK set.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_service_user_key_response import V1beta1GetServiceUserKeyResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to get a key for.
    key_id = 'key_id_example' # str | The unique ID of the key to get.

    try:
        # Get service user key
        api_response = api_instance.frontier_service_get_service_user_key(id, key_id)
        print("The response of ServiceUserApi->frontier_service_get_service_user_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_get_service_user_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to get a key for. | 
 **key_id** | **str**| The unique ID of the key to get. | 

### Return type

[**V1beta1GetServiceUserKeyResponse**](V1beta1GetServiceUserKeyResponse.md)

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

# **frontier_service_list_service_user_keys**
> V1beta1ListServiceUserKeysResponse frontier_service_list_service_user_keys(id)

List service user keys

List all the keys of a service user with its details except jwk.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_service_user_keys_response import V1beta1ListServiceUserKeysResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to list keys for.

    try:
        # List service user keys
        api_response = api_instance.frontier_service_list_service_user_keys(id)
        print("The response of ServiceUserApi->frontier_service_list_service_user_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_list_service_user_keys: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to list keys for. | 

### Return type

[**V1beta1ListServiceUserKeysResponse**](V1beta1ListServiceUserKeysResponse.md)

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

# **frontier_service_list_service_user_secrets**
> V1beta1ListServiceUserSecretsResponse frontier_service_list_service_user_secrets(id)

List service user secrets

List all the secrets of a service user.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_service_user_secrets_response import V1beta1ListServiceUserSecretsResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    id = 'id_example' # str | The unique ID of the service user to list secrets for.

    try:
        # List service user secrets
        api_response = api_instance.frontier_service_list_service_user_secrets(id)
        print("The response of ServiceUserApi->frontier_service_list_service_user_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_list_service_user_secrets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the service user to list secrets for. | 

### Return type

[**V1beta1ListServiceUserSecretsResponse**](V1beta1ListServiceUserSecretsResponse.md)

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

# **frontier_service_list_service_users**
> V1beta1ListServiceUsersResponse frontier_service_list_service_users(org_id, state=state)

List org service users

Returns the service user of an organization in a Frontier instance. It can be filter by it's state

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_service_users_response import V1beta1ListServiceUsersResponse
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
    api_instance = frontier_api.ServiceUserApi(api_client)
    org_id = 'org_id_example' # str | The organization ID to filter service users by.
    state = 'state_example' # str | The state to filter by. It can be enabled or disabled. (optional)

    try:
        # List org service users
        api_response = api_instance.frontier_service_list_service_users(org_id, state=state)
        print("The response of ServiceUserApi->frontier_service_list_service_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUserApi->frontier_service_list_service_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization ID to filter service users by. | 
 **state** | **str**| The state to filter by. It can be enabled or disabled. | [optional] 

### Return type

[**V1beta1ListServiceUsersResponse**](V1beta1ListServiceUsersResponse.md)

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

