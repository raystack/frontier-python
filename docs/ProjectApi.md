# frontier_api.ProjectApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_list_projects**](ProjectApi.md#admin_service_list_projects) | **GET** /v1beta1/admin/projects | List all projects
[**frontier_service_create_project**](ProjectApi.md#frontier_service_create_project) | **POST** /v1beta1/projects | Create project
[**frontier_service_delete_project**](ProjectApi.md#frontier_service_delete_project) | **DELETE** /v1beta1/projects/{id} | Delete Project
[**frontier_service_disable_project**](ProjectApi.md#frontier_service_disable_project) | **POST** /v1beta1/projects/{id}/disable | Disable project
[**frontier_service_enable_project**](ProjectApi.md#frontier_service_enable_project) | **POST** /v1beta1/projects/{id}/enable | Enable project
[**frontier_service_get_project**](ProjectApi.md#frontier_service_get_project) | **GET** /v1beta1/projects/{id} | Get project
[**frontier_service_list_project_admins**](ProjectApi.md#frontier_service_list_project_admins) | **GET** /v1beta1/projects/{id}/admins | List project admins
[**frontier_service_list_project_groups**](ProjectApi.md#frontier_service_list_project_groups) | **GET** /v1beta1/projects/{id}/groups | List project groups
[**frontier_service_list_project_service_users**](ProjectApi.md#frontier_service_list_project_service_users) | **GET** /v1beta1/projects/{id}/serviceusers | List project serviceusers
[**frontier_service_list_project_users**](ProjectApi.md#frontier_service_list_project_users) | **GET** /v1beta1/projects/{id}/users | List project users
[**frontier_service_update_project**](ProjectApi.md#frontier_service_update_project) | **PUT** /v1beta1/projects/{id} | Update project


# **admin_service_list_projects**
> V1beta1ListProjectsResponse admin_service_list_projects(org_id=org_id, state=state)

List all projects

Lists all the projects from all the organizations in a Frontier instance. It can be filtered by organization and state.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_projects_response import V1beta1ListProjectsResponse
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
    api_instance = frontier_api.ProjectApi(api_client)
    org_id = 'org_id_example' # str | The organization id to filter by. (optional)
    state = 'state_example' # str | The state to filter by. It can be enabled or disabled. (optional)

    try:
        # List all projects
        api_response = api_instance.admin_service_list_projects(org_id=org_id, state=state)
        print("The response of ProjectApi->admin_service_list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->admin_service_list_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization id to filter by. | [optional] 
 **state** | **str**| The state to filter by. It can be enabled or disabled. | [optional] 

### Return type

[**V1beta1ListProjectsResponse**](V1beta1ListProjectsResponse.md)

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

# **frontier_service_create_project**
> V1beta1CreateProjectResponse frontier_service_create_project(body)

Create project

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_project_response import V1beta1CreateProjectResponse
from frontier_api.models.v1beta1_project_request_body import V1beta1ProjectRequestBody
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
    api_instance = frontier_api.ProjectApi(api_client)
    body = frontier_api.V1beta1ProjectRequestBody() # V1beta1ProjectRequestBody | 

    try:
        # Create project
        api_response = api_instance.frontier_service_create_project(body)
        print("The response of ProjectApi->frontier_service_create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_create_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ProjectRequestBody**](V1beta1ProjectRequestBody.md)|  | 

### Return type

[**V1beta1CreateProjectResponse**](V1beta1CreateProjectResponse.md)

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

# **frontier_service_delete_project**
> object frontier_service_delete_project(id)

Delete Project

Delete a project all of its relations permanently.

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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Project
        api_response = api_instance.frontier_service_delete_project(id)
        print("The response of ProjectApi->frontier_service_delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_delete_project: %s\n" % e)
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

# **frontier_service_disable_project**
> object frontier_service_disable_project(id, body)

Disable project

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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Disable project
        api_response = api_instance.frontier_service_disable_project(id, body)
        print("The response of ProjectApi->frontier_service_disable_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_disable_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

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

# **frontier_service_enable_project**
> object frontier_service_enable_project(id, body)

Enable project

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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Enable project
        api_response = api_instance.frontier_service_enable_project(id, body)
        print("The response of ProjectApi->frontier_service_enable_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_enable_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

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

# **frontier_service_get_project**
> V1beta1GetProjectResponse frontier_service_get_project(id)

Get project

Returns a project by ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_project_response import V1beta1GetProjectResponse
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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get project
        api_response = api_instance.frontier_service_get_project(id)
        print("The response of ProjectApi->frontier_service_get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_get_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1GetProjectResponse**](V1beta1GetProjectResponse.md)

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

# **frontier_service_list_project_admins**
> V1beta1ListProjectAdminsResponse frontier_service_list_project_admins(id)

List project admins

Returns a collection of admins of a project

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_project_admins_response import V1beta1ListProjectAdminsResponse
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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 

    try:
        # List project admins
        api_response = api_instance.frontier_service_list_project_admins(id)
        print("The response of ProjectApi->frontier_service_list_project_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_list_project_admins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListProjectAdminsResponse**](V1beta1ListProjectAdminsResponse.md)

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

# **frontier_service_list_project_groups**
> V1beta1ListProjectGroupsResponse frontier_service_list_project_groups(id, with_roles=with_roles)

List project groups

Returns a collection of groups of a project.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_project_groups_response import V1beta1ListProjectGroupsResponse
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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 
    with_roles = True # bool |  (optional)

    try:
        # List project groups
        api_response = api_instance.frontier_service_list_project_groups(id, with_roles=with_roles)
        print("The response of ProjectApi->frontier_service_list_project_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_list_project_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **with_roles** | **bool**|  | [optional] 

### Return type

[**V1beta1ListProjectGroupsResponse**](V1beta1ListProjectGroupsResponse.md)

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

# **frontier_service_list_project_service_users**
> V1beta1ListProjectServiceUsersResponse frontier_service_list_project_service_users(id, with_roles=with_roles)

List project serviceusers

Returns a collection of users of a project.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_project_service_users_response import V1beta1ListProjectServiceUsersResponse
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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 
    with_roles = True # bool |  (optional)

    try:
        # List project serviceusers
        api_response = api_instance.frontier_service_list_project_service_users(id, with_roles=with_roles)
        print("The response of ProjectApi->frontier_service_list_project_service_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_list_project_service_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **with_roles** | **bool**|  | [optional] 

### Return type

[**V1beta1ListProjectServiceUsersResponse**](V1beta1ListProjectServiceUsersResponse.md)

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

# **frontier_service_list_project_users**
> V1beta1ListProjectUsersResponse frontier_service_list_project_users(id, permission_filter=permission_filter, with_roles=with_roles)

List project users

Returns a collection of users of a project. Filter by user permissions is supported.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_project_users_response import V1beta1ListProjectUsersResponse
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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 
    permission_filter = 'permission_filter_example' # str |  (optional)
    with_roles = True # bool |  (optional)

    try:
        # List project users
        api_response = api_instance.frontier_service_list_project_users(id, permission_filter=permission_filter, with_roles=with_roles)
        print("The response of ProjectApi->frontier_service_list_project_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_list_project_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **permission_filter** | **str**|  | [optional] 
 **with_roles** | **bool**|  | [optional] 

### Return type

[**V1beta1ListProjectUsersResponse**](V1beta1ListProjectUsersResponse.md)

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

# **frontier_service_update_project**
> V1beta1UpdateProjectResponse frontier_service_update_project(id, body)

Update project

Updates a project by ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_project_request_body import V1beta1ProjectRequestBody
from frontier_api.models.v1beta1_update_project_response import V1beta1UpdateProjectResponse
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
    api_instance = frontier_api.ProjectApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.V1beta1ProjectRequestBody() # V1beta1ProjectRequestBody | 

    try:
        # Update project
        api_response = api_instance.frontier_service_update_project(id, body)
        print("The response of ProjectApi->frontier_service_update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->frontier_service_update_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**V1beta1ProjectRequestBody**](V1beta1ProjectRequestBody.md)|  | 

### Return type

[**V1beta1UpdateProjectResponse**](V1beta1UpdateProjectResponse.md)

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

