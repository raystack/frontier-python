# frontier_api.GroupApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_list_groups**](GroupApi.md#admin_service_list_groups) | **GET** /v1beta1/admin/groups | List all groups
[**frontier_service_add_group_users**](GroupApi.md#frontier_service_add_group_users) | **POST** /v1beta1/organizations/{orgId}/groups/{id}/users | Add group user
[**frontier_service_create_group**](GroupApi.md#frontier_service_create_group) | **POST** /v1beta1/organizations/{orgId}/groups | Create group
[**frontier_service_delete_group**](GroupApi.md#frontier_service_delete_group) | **DELETE** /v1beta1/organizations/{orgId}/groups/{id} | Delete group
[**frontier_service_disable_group**](GroupApi.md#frontier_service_disable_group) | **POST** /v1beta1/organizations/{orgId}/groups/{id}/disable | Disable group
[**frontier_service_enable_group**](GroupApi.md#frontier_service_enable_group) | **POST** /v1beta1/organizations/{orgId}/groups/{id}/enable | Enable group
[**frontier_service_get_group**](GroupApi.md#frontier_service_get_group) | **GET** /v1beta1/organizations/{orgId}/groups/{id} | Get group
[**frontier_service_list_group_users**](GroupApi.md#frontier_service_list_group_users) | **GET** /v1beta1/organizations/{orgId}/groups/{id}/users | List group users
[**frontier_service_list_organization_groups**](GroupApi.md#frontier_service_list_organization_groups) | **GET** /v1beta1/organizations/{orgId}/groups | List organization groups
[**frontier_service_remove_group_user**](GroupApi.md#frontier_service_remove_group_user) | **DELETE** /v1beta1/organizations/{orgId}/groups/{id}/users/{userId} | Remove group user
[**frontier_service_update_group**](GroupApi.md#frontier_service_update_group) | **PUT** /v1beta1/organizations/{orgId}/groups/{id} | Update group


# **admin_service_list_groups**
> V1beta1ListGroupsResponse admin_service_list_groups(org_id=org_id, state=state)

List all groups

Lists all the groups from all the organizations in a Frontier instance. It can be filtered by organization and state.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_groups_response import V1beta1ListGroupsResponse
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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | The organization id to filter by. (optional)
    state = 'state_example' # str | The state to filter by. It can be enabled or disabled. (optional)

    try:
        # List all groups
        api_response = api_instance.admin_service_list_groups(org_id=org_id, state=state)
        print("The response of GroupApi->admin_service_list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->admin_service_list_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization id to filter by. | [optional] 
 **state** | **str**| The state to filter by. It can be enabled or disabled. | [optional] 

### Return type

[**V1beta1ListGroupsResponse**](V1beta1ListGroupsResponse.md)

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

# **frontier_service_add_group_users**
> object frontier_service_add_group_users(org_id, id, body)

Add group user

Adds a principle(user and service-users) to a group, existing users in the group will be ignored. A group can't have nested groups as members.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_add_group_users_request import FrontierServiceAddGroupUsersRequest
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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    body = frontier_api.FrontierServiceAddGroupUsersRequest() # FrontierServiceAddGroupUsersRequest | 

    try:
        # Add group user
        api_response = api_instance.frontier_service_add_group_users(org_id, id, body)
        print("The response of GroupApi->frontier_service_add_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_add_group_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**FrontierServiceAddGroupUsersRequest**](FrontierServiceAddGroupUsersRequest.md)|  | 

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

# **frontier_service_create_group**
> V1beta1CreateGroupResponse frontier_service_create_group(org_id, body)

Create group

Create a new group in an organization which serves as a container for users. The group can be assigned roles and permissions and can be used to manage access to resources. Also a group can also be assigned to other groups.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_group_response import V1beta1CreateGroupResponse
from frontier_api.models.v1beta1_group_request_body import V1beta1GroupRequestBody
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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | The organization ID to which the group belongs to.
    body = frontier_api.V1beta1GroupRequestBody() # V1beta1GroupRequestBody | 

    try:
        # Create group
        api_response = api_instance.frontier_service_create_group(org_id, body)
        print("The response of GroupApi->frontier_service_create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_create_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization ID to which the group belongs to. | 
 **body** | [**V1beta1GroupRequestBody**](V1beta1GroupRequestBody.md)|  | 

### Return type

[**V1beta1CreateGroupResponse**](V1beta1CreateGroupResponse.md)

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

# **frontier_service_delete_group**
> object frontier_service_delete_group(org_id, id)

Delete group

Delete an organization group permanently and all of its relations

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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Delete group
        api_response = api_instance.frontier_service_delete_group(org_id, id)
        print("The response of GroupApi->frontier_service_delete_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_delete_group: %s\n" % e)
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

# **frontier_service_disable_group**
> object frontier_service_disable_group(org_id, id, body)

Disable group

Sets the state of the group as disabled. The group will not be available for access control and the existing users in the group will not be able to access any resources that are assigned to the group. No other users can be added to the group while it is disabled.

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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Disable group
        api_response = api_instance.frontier_service_disable_group(org_id, id, body)
        print("The response of GroupApi->frontier_service_disable_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_disable_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
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

# **frontier_service_enable_group**
> object frontier_service_enable_group(org_id, id, body)

Enable group

Sets the state of the group as enabled. The `enabled` flag is used to determine if the group can be used for access control.

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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Enable group
        api_response = api_instance.frontier_service_enable_group(org_id, id, body)
        print("The response of GroupApi->frontier_service_enable_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_enable_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
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

# **frontier_service_get_group**
> V1beta1GetGroupResponse frontier_service_get_group(org_id, id, with_members=with_members)

Get group

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_group_response import V1beta1GetGroupResponse
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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    with_members = True # bool |  (optional)

    try:
        # Get group
        api_response = api_instance.frontier_service_get_group(org_id, id, with_members=with_members)
        print("The response of GroupApi->frontier_service_get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_get_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 
 **with_members** | **bool**|  | [optional] 

### Return type

[**V1beta1GetGroupResponse**](V1beta1GetGroupResponse.md)

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

# **frontier_service_list_group_users**
> V1beta1ListGroupUsersResponse frontier_service_list_group_users(org_id, id, with_roles=with_roles)

List group users

Returns a list of users that belong to a group.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_group_users_response import V1beta1ListGroupUsersResponse
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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    with_roles = True # bool |  (optional)

    try:
        # List group users
        api_response = api_instance.frontier_service_list_group_users(org_id, id, with_roles=with_roles)
        print("The response of GroupApi->frontier_service_list_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_list_group_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 
 **with_roles** | **bool**|  | [optional] 

### Return type

[**V1beta1ListGroupUsersResponse**](V1beta1ListGroupUsersResponse.md)

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

# **frontier_service_list_organization_groups**
> V1beta1ListOrganizationGroupsResponse frontier_service_list_organization_groups(org_id, state=state, group_ids=group_ids, with_members=with_members)

List organization groups

Get all groups that belong to an organization. The results can be filtered by state which can be either be enabled or disabled.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_groups_response import V1beta1ListOrganizationGroupsResponse
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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    state = 'state_example' # str | The state of the group to filter by. It can be enabled or disabled. (optional)
    group_ids = ['group_ids_example'] # List[str] |  (optional)
    with_members = True # bool |  (optional)

    try:
        # List organization groups
        api_response = api_instance.frontier_service_list_organization_groups(org_id, state=state, group_ids=group_ids, with_members=with_members)
        print("The response of GroupApi->frontier_service_list_organization_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_list_organization_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **state** | **str**| The state of the group to filter by. It can be enabled or disabled. | [optional] 
 **group_ids** | [**List[str]**](str.md)|  | [optional] 
 **with_members** | **bool**|  | [optional] 

### Return type

[**V1beta1ListOrganizationGroupsResponse**](V1beta1ListOrganizationGroupsResponse.md)

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

# **frontier_service_remove_group_user**
> object frontier_service_remove_group_user(org_id, id, user_id)

Remove group user

Removes a principle(user and service-users) from a group. If the user is not in the group, the request will succeed but no changes will be made.

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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove group user
        api_response = api_instance.frontier_service_remove_group_user(org_id, id, user_id)
        print("The response of GroupApi->frontier_service_remove_group_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_remove_group_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 
 **user_id** | **str**|  | 

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

# **frontier_service_update_group**
> V1beta1UpdateGroupResponse frontier_service_update_group(org_id, id, body)

Update group

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_group_request_body import V1beta1GroupRequestBody
from frontier_api.models.v1beta1_update_group_response import V1beta1UpdateGroupResponse
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
    api_instance = frontier_api.GroupApi(api_client)
    org_id = 'org_id_example' # str | The organization ID to which the group belongs to.
    id = 'id_example' # str | 
    body = frontier_api.V1beta1GroupRequestBody() # V1beta1GroupRequestBody | 

    try:
        # Update group
        api_response = api_instance.frontier_service_update_group(org_id, id, body)
        print("The response of GroupApi->frontier_service_update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->frontier_service_update_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization ID to which the group belongs to. | 
 **id** | **str**|  | 
 **body** | [**V1beta1GroupRequestBody**](V1beta1GroupRequestBody.md)|  | 

### Return type

[**V1beta1UpdateGroupResponse**](V1beta1UpdateGroupResponse.md)

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

