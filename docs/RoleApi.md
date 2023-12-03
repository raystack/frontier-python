# frontier_api.RoleApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_create_role**](RoleApi.md#admin_service_create_role) | **POST** /v1beta1/roles | Create platform role
[**admin_service_delete_role**](RoleApi.md#admin_service_delete_role) | **DELETE** /v1beta1/roles/{id} | Delete platform role
[**admin_service_update_role**](RoleApi.md#admin_service_update_role) | **PUT** /v1beta1/roles/{id} | Update role
[**frontier_service_create_organization_role**](RoleApi.md#frontier_service_create_organization_role) | **POST** /v1beta1/organizations/{orgId}/roles | Create organization role
[**frontier_service_delete_organization_role**](RoleApi.md#frontier_service_delete_organization_role) | **DELETE** /v1beta1/organizations/{orgId}/roles/{id} | Delete organization role
[**frontier_service_get_organization_role**](RoleApi.md#frontier_service_get_organization_role) | **GET** /v1beta1/organizations/{orgId}/roles/{id} | Get organization role
[**frontier_service_list_organization_roles**](RoleApi.md#frontier_service_list_organization_roles) | **GET** /v1beta1/organizations/{orgId}/roles | List organization roles
[**frontier_service_list_roles**](RoleApi.md#frontier_service_list_roles) | **GET** /v1beta1/roles | List platform roles
[**frontier_service_update_organization_role**](RoleApi.md#frontier_service_update_organization_role) | **PUT** /v1beta1/organizations/{orgId}/roles/{id} | Update organization role


# **admin_service_create_role**
> V1beta1CreateRoleResponse admin_service_create_role(body)

Create platform role

Creates a platform wide role. It can be used to grant permissions to all the resources in a Frontier instance.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_role_response import V1beta1CreateRoleResponse
from frontier_api.models.v1beta1_role_request_body import V1beta1RoleRequestBody
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
    api_instance = frontier_api.RoleApi(api_client)
    body = frontier_api.V1beta1RoleRequestBody() # V1beta1RoleRequestBody | 

    try:
        # Create platform role
        api_response = api_instance.admin_service_create_role(body)
        print("The response of RoleApi->admin_service_create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->admin_service_create_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1RoleRequestBody**](V1beta1RoleRequestBody.md)|  | 

### Return type

[**V1beta1CreateRoleResponse**](V1beta1CreateRoleResponse.md)

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

# **admin_service_delete_role**
> object admin_service_delete_role(id)

Delete platform role

Delete a platform wide role and all of its relations.

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
    api_instance = frontier_api.RoleApi(api_client)
    id = 'id_example' # str | The role id to delete.

    try:
        # Delete platform role
        api_response = api_instance.admin_service_delete_role(id)
        print("The response of RoleApi->admin_service_delete_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->admin_service_delete_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The role id to delete. | 

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

# **admin_service_update_role**
> V1beta1UpdateRoleResponse admin_service_update_role(id, body)

Update role

Update a role title, description and permissions.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_role_request_body import V1beta1RoleRequestBody
from frontier_api.models.v1beta1_update_role_response import V1beta1UpdateRoleResponse
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
    api_instance = frontier_api.RoleApi(api_client)
    id = 'id_example' # str | The role id to update.
    body = frontier_api.V1beta1RoleRequestBody() # V1beta1RoleRequestBody | 

    try:
        # Update role
        api_response = api_instance.admin_service_update_role(id, body)
        print("The response of RoleApi->admin_service_update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->admin_service_update_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The role id to update. | 
 **body** | [**V1beta1RoleRequestBody**](V1beta1RoleRequestBody.md)|  | 

### Return type

[**V1beta1UpdateRoleResponse**](V1beta1UpdateRoleResponse.md)

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

# **frontier_service_create_organization_role**
> V1beta1CreateOrganizationRoleResponse frontier_service_create_organization_role(org_id, body)

Create organization role

Create a custom role under an organization. This custom role will only be available for assignment to the principles within the organization.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_organization_role_response import V1beta1CreateOrganizationRoleResponse
from frontier_api.models.v1beta1_role_request_body import V1beta1RoleRequestBody
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
    api_instance = frontier_api.RoleApi(api_client)
    org_id = 'org_id_example' # str | The organization ID to which the role belongs to.
    body = frontier_api.V1beta1RoleRequestBody() # V1beta1RoleRequestBody | 

    try:
        # Create organization role
        api_response = api_instance.frontier_service_create_organization_role(org_id, body)
        print("The response of RoleApi->frontier_service_create_organization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->frontier_service_create_organization_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization ID to which the role belongs to. | 
 **body** | [**V1beta1RoleRequestBody**](V1beta1RoleRequestBody.md)|  | 

### Return type

[**V1beta1CreateOrganizationRoleResponse**](V1beta1CreateOrganizationRoleResponse.md)

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

# **frontier_service_delete_organization_role**
> object frontier_service_delete_organization_role(org_id, id)

Delete organization role

Delete a custom role and all of its relations under an organization permanently.

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
    api_instance = frontier_api.RoleApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Delete organization role
        api_response = api_instance.frontier_service_delete_organization_role(org_id, id)
        print("The response of RoleApi->frontier_service_delete_organization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->frontier_service_delete_organization_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
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

# **frontier_service_get_organization_role**
> V1beta1GetOrganizationRoleResponse frontier_service_get_organization_role(org_id, id)

Get organization role

Returns a custom role under an organization along with its associated permissions

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_organization_role_response import V1beta1GetOrganizationRoleResponse
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
    api_instance = frontier_api.RoleApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Get organization role
        api_response = api_instance.frontier_service_get_organization_role(org_id, id)
        print("The response of RoleApi->frontier_service_get_organization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->frontier_service_get_organization_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**V1beta1GetOrganizationRoleResponse**](V1beta1GetOrganizationRoleResponse.md)

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

# **frontier_service_list_organization_roles**
> V1beta1ListOrganizationRolesResponse frontier_service_list_organization_roles(org_id, state=state, scopes=scopes)

List organization roles

Returns a list of custom roles created under an organization with their associated permissions

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_roles_response import V1beta1ListOrganizationRolesResponse
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
    api_instance = frontier_api.RoleApi(api_client)
    org_id = 'org_id_example' # str | 
    state = 'state_example' # str |  (optional)
    scopes = ['scopes_example'] # List[str] |  (optional)

    try:
        # List organization roles
        api_response = api_instance.frontier_service_list_organization_roles(org_id, state=state, scopes=scopes)
        print("The response of RoleApi->frontier_service_list_organization_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->frontier_service_list_organization_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **state** | **str**|  | [optional] 
 **scopes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**V1beta1ListOrganizationRolesResponse**](V1beta1ListOrganizationRolesResponse.md)

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

# **frontier_service_list_roles**
> V1beta1ListRolesResponse frontier_service_list_roles(state=state, scopes=scopes)

List platform roles

Returns a list of platform wide roles available in enitre Frontier instance along with their associated permissions

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_roles_response import V1beta1ListRolesResponse
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
    api_instance = frontier_api.RoleApi(api_client)
    state = 'state_example' # str |  (optional)
    scopes = ['scopes_example'] # List[str] |  (optional)

    try:
        # List platform roles
        api_response = api_instance.frontier_service_list_roles(state=state, scopes=scopes)
        print("The response of RoleApi->frontier_service_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->frontier_service_list_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | [optional] 
 **scopes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**V1beta1ListRolesResponse**](V1beta1ListRolesResponse.md)

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

# **frontier_service_update_organization_role**
> V1beta1UpdateOrganizationRoleResponse frontier_service_update_organization_role(org_id, id, body)

Update organization role

Update a custom role under an organization. This custom role will only be available for assignment to the principles within the organization.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_role_request_body import V1beta1RoleRequestBody
from frontier_api.models.v1beta1_update_organization_role_response import V1beta1UpdateOrganizationRoleResponse
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
    api_instance = frontier_api.RoleApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    body = frontier_api.V1beta1RoleRequestBody() # V1beta1RoleRequestBody | 

    try:
        # Update organization role
        api_response = api_instance.frontier_service_update_organization_role(org_id, id, body)
        print("The response of RoleApi->frontier_service_update_organization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->frontier_service_update_organization_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**V1beta1RoleRequestBody**](V1beta1RoleRequestBody.md)|  | 

### Return type

[**V1beta1UpdateOrganizationRoleResponse**](V1beta1UpdateOrganizationRoleResponse.md)

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

