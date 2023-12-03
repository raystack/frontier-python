# frontier_api.ResourceApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_list_resources**](ResourceApi.md#admin_service_list_resources) | **GET** /v1beta1/admin/resources | List all resources
[**frontier_service_create_project_resource**](ResourceApi.md#frontier_service_create_project_resource) | **POST** /v1beta1/projects/{projectId}/resources | Create resource
[**frontier_service_delete_project_resource**](ResourceApi.md#frontier_service_delete_project_resource) | **DELETE** /v1beta1/projects/{projectId}/resources/{id} | Delete resource
[**frontier_service_get_project_resource**](ResourceApi.md#frontier_service_get_project_resource) | **GET** /v1beta1/projects/{projectId}/resources/{id} | Get resource
[**frontier_service_list_project_resources**](ResourceApi.md#frontier_service_list_project_resources) | **GET** /v1beta1/projects/{projectId}/resources | Get all resources
[**frontier_service_update_project_resource**](ResourceApi.md#frontier_service_update_project_resource) | **PUT** /v1beta1/projects/{projectId}/resources/{id} | Update resource


# **admin_service_list_resources**
> V1beta1ListResourcesResponse admin_service_list_resources(user_id=user_id, project_id=project_id, organization_id=organization_id, namespace=namespace)

List all resources

Lists all the resources from all the organizations in a Frontier instance. It can be filtered by user, project, organization and namespace.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_resources_response import V1beta1ListResourcesResponse
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
    api_instance = frontier_api.ResourceApi(api_client)
    user_id = 'user_id_example' # str | The user id to filter by. (optional)
    project_id = 'project_id_example' # str | The project id to filter by. (optional)
    organization_id = 'organization_id_example' # str | The organization id to filter by. (optional)
    namespace = 'namespace_example' # str | The namespace to filter by. (optional)

    try:
        # List all resources
        api_response = api_instance.admin_service_list_resources(user_id=user_id, project_id=project_id, organization_id=organization_id, namespace=namespace)
        print("The response of ResourceApi->admin_service_list_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceApi->admin_service_list_resources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id to filter by. | [optional] 
 **project_id** | **str**| The project id to filter by. | [optional] 
 **organization_id** | **str**| The organization id to filter by. | [optional] 
 **namespace** | **str**| The namespace to filter by. | [optional] 

### Return type

[**V1beta1ListResourcesResponse**](V1beta1ListResourcesResponse.md)

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

# **frontier_service_create_project_resource**
> V1beta1CreateProjectResourceResponse frontier_service_create_project_resource(project_id, body, id=id)

Create resource

Creates a resource in a project

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_project_resource_response import V1beta1CreateProjectResourceResponse
from frontier_api.models.v1beta1_resource_request_body import V1beta1ResourceRequestBody
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
    api_instance = frontier_api.ResourceApi(api_client)
    project_id = 'project_id_example' # str | project uuid or name
    body = frontier_api.V1beta1ResourceRequestBody() # V1beta1ResourceRequestBody | 
    id = 'id_example' # str | Autogenerated if skipped. (optional)

    try:
        # Create resource
        api_response = api_instance.frontier_service_create_project_resource(project_id, body, id=id)
        print("The response of ResourceApi->frontier_service_create_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceApi->frontier_service_create_project_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| project uuid or name | 
 **body** | [**V1beta1ResourceRequestBody**](V1beta1ResourceRequestBody.md)|  | 
 **id** | **str**| Autogenerated if skipped. | [optional] 

### Return type

[**V1beta1CreateProjectResourceResponse**](V1beta1CreateProjectResourceResponse.md)

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

# **frontier_service_delete_project_resource**
> object frontier_service_delete_project_resource(project_id, id)

Delete resource

Deletes a resource from a project permanently

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
    api_instance = frontier_api.ResourceApi(api_client)
    project_id = 'project_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Delete resource
        api_response = api_instance.frontier_service_delete_project_resource(project_id, id)
        print("The response of ResourceApi->frontier_service_delete_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceApi->frontier_service_delete_project_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **frontier_service_get_project_resource**
> V1beta1GetProjectResourceResponse frontier_service_get_project_resource(project_id, id)

Get resource

Returns a project resource by ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_project_resource_response import V1beta1GetProjectResourceResponse
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
    api_instance = frontier_api.ResourceApi(api_client)
    project_id = 'project_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Get resource
        api_response = api_instance.frontier_service_get_project_resource(project_id, id)
        print("The response of ResourceApi->frontier_service_get_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceApi->frontier_service_get_project_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**V1beta1GetProjectResourceResponse**](V1beta1GetProjectResourceResponse.md)

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

# **frontier_service_list_project_resources**
> V1beta1ListProjectResourcesResponse frontier_service_list_project_resources(project_id, namespace=namespace)

Get all resources

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_project_resources_response import V1beta1ListProjectResourcesResponse
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
    api_instance = frontier_api.ResourceApi(api_client)
    project_id = 'project_id_example' # str | 
    namespace = 'namespace_example' # str |  (optional)

    try:
        # Get all resources
        api_response = api_instance.frontier_service_list_project_resources(project_id, namespace=namespace)
        print("The response of ResourceApi->frontier_service_list_project_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceApi->frontier_service_list_project_resources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **namespace** | **str**|  | [optional] 

### Return type

[**V1beta1ListProjectResourcesResponse**](V1beta1ListProjectResourcesResponse.md)

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

# **frontier_service_update_project_resource**
> V1beta1UpdateProjectResourceResponse frontier_service_update_project_resource(project_id, id, body)

Update resource

Updates a resource in a project

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_resource_request_body import V1beta1ResourceRequestBody
from frontier_api.models.v1beta1_update_project_resource_response import V1beta1UpdateProjectResourceResponse
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
    api_instance = frontier_api.ResourceApi(api_client)
    project_id = 'project_id_example' # str | 
    id = 'id_example' # str | 
    body = frontier_api.V1beta1ResourceRequestBody() # V1beta1ResourceRequestBody | 

    try:
        # Update resource
        api_response = api_instance.frontier_service_update_project_resource(project_id, id, body)
        print("The response of ResourceApi->frontier_service_update_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceApi->frontier_service_update_project_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**V1beta1ResourceRequestBody**](V1beta1ResourceRequestBody.md)|  | 

### Return type

[**V1beta1UpdateProjectResourceResponse**](V1beta1UpdateProjectResourceResponse.md)

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

