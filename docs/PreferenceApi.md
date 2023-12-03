# frontier_api.PreferenceApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_create_preferences**](PreferenceApi.md#admin_service_create_preferences) | **POST** /v1beta1/preferences | Create platform preferences
[**admin_service_list_preferences**](PreferenceApi.md#admin_service_list_preferences) | **GET** /v1beta1/preferences | List platform preferences
[**frontier_service_create_current_user_preferences**](PreferenceApi.md#frontier_service_create_current_user_preferences) | **POST** /v1beta1/users/self/preferences | Create current user preferences
[**frontier_service_create_group_preferences**](PreferenceApi.md#frontier_service_create_group_preferences) | **POST** /v1beta1/groups/{id}/preferences | Create group preferences
[**frontier_service_create_organization_preferences**](PreferenceApi.md#frontier_service_create_organization_preferences) | **POST** /v1beta1/organizations/{id}/preferences | Create organization preferences
[**frontier_service_create_project_preferences**](PreferenceApi.md#frontier_service_create_project_preferences) | **POST** /v1beta1/projects/{id}/preferences | Create project preferences
[**frontier_service_create_user_preferences**](PreferenceApi.md#frontier_service_create_user_preferences) | **POST** /v1beta1/users/{id}/preferences | Create user preferences
[**frontier_service_describe_preferences**](PreferenceApi.md#frontier_service_describe_preferences) | **GET** /v1beta1/preferences/traits | Describe preferences
[**frontier_service_list_current_user_preferences**](PreferenceApi.md#frontier_service_list_current_user_preferences) | **GET** /v1beta1/users/self/preferences | List current user preferences
[**frontier_service_list_group_preferences**](PreferenceApi.md#frontier_service_list_group_preferences) | **GET** /v1beta1/groups/{id}/preferences | List group preferences
[**frontier_service_list_organization_preferences**](PreferenceApi.md#frontier_service_list_organization_preferences) | **GET** /v1beta1/organizations/{id}/preferences | List organization preferences
[**frontier_service_list_project_preferences**](PreferenceApi.md#frontier_service_list_project_preferences) | **GET** /v1beta1/projects/{id}/preferences | List project preferences
[**frontier_service_list_user_preferences**](PreferenceApi.md#frontier_service_list_user_preferences) | **GET** /v1beta1/users/{id}/preferences | List user preferences


# **admin_service_create_preferences**
> V1beta1CreatePreferencesResponse admin_service_create_preferences(body)

Create platform preferences

Create new platform preferences. The platform preferences **name** must be unique within the platform and can contain only alphanumeric characters, dashes and underscores.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_preferences_request import V1beta1CreatePreferencesRequest
from frontier_api.models.v1beta1_create_preferences_response import V1beta1CreatePreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    body = frontier_api.V1beta1CreatePreferencesRequest() # V1beta1CreatePreferencesRequest | 

    try:
        # Create platform preferences
        api_response = api_instance.admin_service_create_preferences(body)
        print("The response of PreferenceApi->admin_service_create_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->admin_service_create_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CreatePreferencesRequest**](V1beta1CreatePreferencesRequest.md)|  | 

### Return type

[**V1beta1CreatePreferencesResponse**](V1beta1CreatePreferencesResponse.md)

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

# **admin_service_list_preferences**
> V1beta1ListPreferencesResponse admin_service_list_preferences()

List platform preferences

Returns a list of all preferences configured on an instance in Frontier. e.g user, project, organization etc

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_preferences_response import V1beta1ListPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)

    try:
        # List platform preferences
        api_response = api_instance.admin_service_list_preferences()
        print("The response of PreferenceApi->admin_service_list_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->admin_service_list_preferences: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListPreferencesResponse**](V1beta1ListPreferencesResponse.md)

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

# **frontier_service_create_current_user_preferences**
> V1beta1CreateCurrentUserPreferencesResponse frontier_service_create_current_user_preferences(body)

Create current user preferences

Create a new user preferences. The user preferences **name** must be unique within the user and can contain only alphanumeric characters, dashes and underscores.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_current_user_preferences_request import V1beta1CreateCurrentUserPreferencesRequest
from frontier_api.models.v1beta1_create_current_user_preferences_response import V1beta1CreateCurrentUserPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    body = frontier_api.V1beta1CreateCurrentUserPreferencesRequest() # V1beta1CreateCurrentUserPreferencesRequest | 

    try:
        # Create current user preferences
        api_response = api_instance.frontier_service_create_current_user_preferences(body)
        print("The response of PreferenceApi->frontier_service_create_current_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_create_current_user_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CreateCurrentUserPreferencesRequest**](V1beta1CreateCurrentUserPreferencesRequest.md)|  | 

### Return type

[**V1beta1CreateCurrentUserPreferencesResponse**](V1beta1CreateCurrentUserPreferencesResponse.md)

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

# **frontier_service_create_group_preferences**
> V1beta1CreateGroupPreferencesResponse frontier_service_create_group_preferences(id, body)

Create group preferences

Create a new group preferences. The group preferences **name** must be unique within the group and can contain only alphanumeric characters, dashes and underscores.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_group_preferences_request import FrontierServiceCreateGroupPreferencesRequest
from frontier_api.models.v1beta1_create_group_preferences_response import V1beta1CreateGroupPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.FrontierServiceCreateGroupPreferencesRequest() # FrontierServiceCreateGroupPreferencesRequest | 

    try:
        # Create group preferences
        api_response = api_instance.frontier_service_create_group_preferences(id, body)
        print("The response of PreferenceApi->frontier_service_create_group_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_create_group_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**FrontierServiceCreateGroupPreferencesRequest**](FrontierServiceCreateGroupPreferencesRequest.md)|  | 

### Return type

[**V1beta1CreateGroupPreferencesResponse**](V1beta1CreateGroupPreferencesResponse.md)

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

# **frontier_service_create_organization_preferences**
> V1beta1CreateOrganizationPreferencesResponse frontier_service_create_organization_preferences(id, body)

Create organization preferences

Create a new organization preferences. The organization preferences **name** must be unique within the organization and can contain only alphanumeric characters, dashes and underscores.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_group_preferences_request import FrontierServiceCreateGroupPreferencesRequest
from frontier_api.models.v1beta1_create_organization_preferences_response import V1beta1CreateOrganizationPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.FrontierServiceCreateGroupPreferencesRequest() # FrontierServiceCreateGroupPreferencesRequest | 

    try:
        # Create organization preferences
        api_response = api_instance.frontier_service_create_organization_preferences(id, body)
        print("The response of PreferenceApi->frontier_service_create_organization_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_create_organization_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**FrontierServiceCreateGroupPreferencesRequest**](FrontierServiceCreateGroupPreferencesRequest.md)|  | 

### Return type

[**V1beta1CreateOrganizationPreferencesResponse**](V1beta1CreateOrganizationPreferencesResponse.md)

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

# **frontier_service_create_project_preferences**
> V1beta1CreateProjectPreferencesResponse frontier_service_create_project_preferences(id, body)

Create project preferences

Create a new project preferences. The project preferences **name** must be unique within the project and can contain only alphanumeric characters, dashes and underscores.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_group_preferences_request import FrontierServiceCreateGroupPreferencesRequest
from frontier_api.models.v1beta1_create_project_preferences_response import V1beta1CreateProjectPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.FrontierServiceCreateGroupPreferencesRequest() # FrontierServiceCreateGroupPreferencesRequest | 

    try:
        # Create project preferences
        api_response = api_instance.frontier_service_create_project_preferences(id, body)
        print("The response of PreferenceApi->frontier_service_create_project_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_create_project_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**FrontierServiceCreateGroupPreferencesRequest**](FrontierServiceCreateGroupPreferencesRequest.md)|  | 

### Return type

[**V1beta1CreateProjectPreferencesResponse**](V1beta1CreateProjectPreferencesResponse.md)

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

# **frontier_service_create_user_preferences**
> V1beta1CreateUserPreferencesResponse frontier_service_create_user_preferences(id, body)

Create user preferences

Create a new user preferences. The user preferences **name** must be unique within the user and can contain only alphanumeric characters, dashes and underscores.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_group_preferences_request import FrontierServiceCreateGroupPreferencesRequest
from frontier_api.models.v1beta1_create_user_preferences_response import V1beta1CreateUserPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.FrontierServiceCreateGroupPreferencesRequest() # FrontierServiceCreateGroupPreferencesRequest | 

    try:
        # Create user preferences
        api_response = api_instance.frontier_service_create_user_preferences(id, body)
        print("The response of PreferenceApi->frontier_service_create_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_create_user_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**FrontierServiceCreateGroupPreferencesRequest**](FrontierServiceCreateGroupPreferencesRequest.md)|  | 

### Return type

[**V1beta1CreateUserPreferencesResponse**](V1beta1CreateUserPreferencesResponse.md)

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

# **frontier_service_describe_preferences**
> V1beta1DescribePreferencesResponse frontier_service_describe_preferences()

Describe preferences

Returns a list of all preferences supported by Frontier.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_describe_preferences_response import V1beta1DescribePreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)

    try:
        # Describe preferences
        api_response = api_instance.frontier_service_describe_preferences()
        print("The response of PreferenceApi->frontier_service_describe_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_describe_preferences: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1DescribePreferencesResponse**](V1beta1DescribePreferencesResponse.md)

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

# **frontier_service_list_current_user_preferences**
> V1beta1ListCurrentUserPreferencesResponse frontier_service_list_current_user_preferences()

List current user preferences

List a user preferences by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_current_user_preferences_response import V1beta1ListCurrentUserPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)

    try:
        # List current user preferences
        api_response = api_instance.frontier_service_list_current_user_preferences()
        print("The response of PreferenceApi->frontier_service_list_current_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_list_current_user_preferences: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListCurrentUserPreferencesResponse**](V1beta1ListCurrentUserPreferencesResponse.md)

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

# **frontier_service_list_group_preferences**
> V1beta1ListGroupPreferencesResponse frontier_service_list_group_preferences(id)

List group preferences

List a group preferences by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_group_preferences_response import V1beta1ListGroupPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # List group preferences
        api_response = api_instance.frontier_service_list_group_preferences(id)
        print("The response of PreferenceApi->frontier_service_list_group_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_list_group_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListGroupPreferencesResponse**](V1beta1ListGroupPreferencesResponse.md)

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

# **frontier_service_list_organization_preferences**
> V1beta1ListOrganizationPreferencesResponse frontier_service_list_organization_preferences(id)

List organization preferences

List an organization preferences by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_preferences_response import V1beta1ListOrganizationPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # List organization preferences
        api_response = api_instance.frontier_service_list_organization_preferences(id)
        print("The response of PreferenceApi->frontier_service_list_organization_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_list_organization_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListOrganizationPreferencesResponse**](V1beta1ListOrganizationPreferencesResponse.md)

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

# **frontier_service_list_project_preferences**
> V1beta1ListProjectPreferencesResponse frontier_service_list_project_preferences(id)

List project preferences

List a project preferences by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_project_preferences_response import V1beta1ListProjectPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # List project preferences
        api_response = api_instance.frontier_service_list_project_preferences(id)
        print("The response of PreferenceApi->frontier_service_list_project_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_list_project_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListProjectPreferencesResponse**](V1beta1ListProjectPreferencesResponse.md)

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

# **frontier_service_list_user_preferences**
> V1beta1ListUserPreferencesResponse frontier_service_list_user_preferences(id)

List user preferences

List a user preferences by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_user_preferences_response import V1beta1ListUserPreferencesResponse
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
    api_instance = frontier_api.PreferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # List user preferences
        api_response = api_instance.frontier_service_list_user_preferences(id)
        print("The response of PreferenceApi->frontier_service_list_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferenceApi->frontier_service_list_user_preferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListUserPreferencesResponse**](V1beta1ListUserPreferencesResponse.md)

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

