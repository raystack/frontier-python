# frontier_api.UserApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_list_all_users**](UserApi.md#admin_service_list_all_users) | **GET** /v1beta1/admin/users | List all users
[**frontier_service_create_user**](UserApi.md#frontier_service_create_user) | **POST** /v1beta1/users | Create user
[**frontier_service_delete_user**](UserApi.md#frontier_service_delete_user) | **DELETE** /v1beta1/users/{id} | Delete user
[**frontier_service_disable_user**](UserApi.md#frontier_service_disable_user) | **POST** /v1beta1/users/{id}/disable | Disable user
[**frontier_service_enable_user**](UserApi.md#frontier_service_enable_user) | **POST** /v1beta1/users/{id}/enable | Enable user
[**frontier_service_get_current_user**](UserApi.md#frontier_service_get_current_user) | **GET** /v1beta1/users/self | Get current user
[**frontier_service_get_user**](UserApi.md#frontier_service_get_user) | **GET** /v1beta1/users/{id} | Get user
[**frontier_service_list_current_user_groups**](UserApi.md#frontier_service_list_current_user_groups) | **GET** /v1beta1/users/self/groups | List my groups
[**frontier_service_list_current_user_invitations**](UserApi.md#frontier_service_list_current_user_invitations) | **GET** /v1beta1/users/self/invitations | List user invitations
[**frontier_service_list_organizations_by_current_user**](UserApi.md#frontier_service_list_organizations_by_current_user) | **GET** /v1beta1/users/self/organizations | Get my organizations
[**frontier_service_list_organizations_by_user**](UserApi.md#frontier_service_list_organizations_by_user) | **GET** /v1beta1/users/{id}/organizations | Get user organizations
[**frontier_service_list_projects_by_current_user**](UserApi.md#frontier_service_list_projects_by_current_user) | **GET** /v1beta1/users/self/projects | Get my projects
[**frontier_service_list_projects_by_user**](UserApi.md#frontier_service_list_projects_by_user) | **GET** /v1beta1/users/{id}/projects | Get user projects
[**frontier_service_list_user_groups**](UserApi.md#frontier_service_list_user_groups) | **GET** /v1beta1/users/{id}/groups | List user groups
[**frontier_service_list_user_invitations**](UserApi.md#frontier_service_list_user_invitations) | **GET** /v1beta1/users/{id}/invitations | List user invitations
[**frontier_service_list_users**](UserApi.md#frontier_service_list_users) | **GET** /v1beta1/users | List public users
[**frontier_service_update_current_user**](UserApi.md#frontier_service_update_current_user) | **PUT** /v1beta1/users/self | Update current user
[**frontier_service_update_user**](UserApi.md#frontier_service_update_user) | **PUT** /v1beta1/users/{id} | Update user


# **admin_service_list_all_users**
> V1beta1ListAllUsersResponse admin_service_list_all_users(page_size=page_size, page_num=page_num, keyword=keyword, org_id=org_id, group_id=group_id, state=state)

List all users

Lists all the users from all the organizations in a Frontier instance. It can be filtered by keyword, organization, group and state.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_all_users_response import V1beta1ListAllUsersResponse
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
    api_instance = frontier_api.UserApi(api_client)
    page_size = 56 # int | The maximum number of users to return per page. The default is 50. (optional)
    page_num = 56 # int | The page number to return. The default is 1. (optional)
    keyword = 'keyword_example' # str | The keyword to search for. It can be a user's name, email,metadata or id. (optional)
    org_id = 'org_id_example' # str | The organization id to filter by. (optional)
    group_id = 'group_id_example' # str | The group id to filter by. (optional)
    state = 'state_example' # str | The state to filter by. It can be enabled or disabled. (optional)

    try:
        # List all users
        api_response = api_instance.admin_service_list_all_users(page_size=page_size, page_num=page_num, keyword=keyword, org_id=org_id, group_id=group_id, state=state)
        print("The response of UserApi->admin_service_list_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->admin_service_list_all_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The maximum number of users to return per page. The default is 50. | [optional] 
 **page_num** | **int**| The page number to return. The default is 1. | [optional] 
 **keyword** | **str**| The keyword to search for. It can be a user&#39;s name, email,metadata or id. | [optional] 
 **org_id** | **str**| The organization id to filter by. | [optional] 
 **group_id** | **str**| The group id to filter by. | [optional] 
 **state** | **str**| The state to filter by. It can be enabled or disabled. | [optional] 

### Return type

[**V1beta1ListAllUsersResponse**](V1beta1ListAllUsersResponse.md)

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

# **frontier_service_create_user**
> V1beta1CreateUserResponse frontier_service_create_user(body)

Create user

Create a user with the given details. A user is not attached to an organization or a group by default,and can be invited to the org/group. The name of the user must be unique within the entire Frontier instance. If a user name is not provided, Frontier automatically generates a name from the user email. The user metadata is validated against the user metaschema. By default the user metaschema contains `labels` and `descriptions` for the user. The `title` field can be optionally added for a user-friendly name. <br/><br/>*Example:*`{\"email\":\"john.doe@raystack.org\",\"title\":\"John Doe\",metadata:{\"label\": {\"key1\": \"value1\"}, \"description\": \"User Description\"}}`

### Example

```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_user_response import V1beta1CreateUserResponse
from frontier_api.models.v1beta1_user_request_body import V1beta1UserRequestBody
from frontier_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:7400
# See configuration.py for a list of all supported configuration parameters.
configuration = frontier_api.Configuration(
    host = "http://127.0.0.1:7400"
)


# Enter a context with an instance of the API client
with frontier_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontier_api.UserApi(api_client)
    body = frontier_api.V1beta1UserRequestBody() # V1beta1UserRequestBody | 

    try:
        # Create user
        api_response = api_instance.frontier_service_create_user(body)
        print("The response of UserApi->frontier_service_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1UserRequestBody**](V1beta1UserRequestBody.md)|  | 

### Return type

[**V1beta1CreateUserResponse**](V1beta1CreateUserResponse.md)

### Authorization

No authorization required

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

# **frontier_service_delete_user**
> object frontier_service_delete_user(id)

Delete user

Delete an user permanently forever and all of its relations (organizations, groups, etc)

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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete user
        api_response = api_instance.frontier_service_delete_user(id)
        print("The response of UserApi->frontier_service_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_delete_user: %s\n" % e)
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

# **frontier_service_disable_user**
> object frontier_service_disable_user(id, body)

Disable user

Sets the state of the user as diabled.The user's membership to groups and organizations will still exist along with all it's roles for access control, but the user will not be able to log in and access the Frontier instance.

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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Disable user
        api_response = api_instance.frontier_service_disable_user(id, body)
        print("The response of UserApi->frontier_service_disable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_disable_user: %s\n" % e)
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

# **frontier_service_enable_user**
> object frontier_service_enable_user(id, body)

Enable user

Sets the state of the user as enabled. The user will be able to log in and access the Frontier instance.

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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Enable user
        api_response = api_instance.frontier_service_enable_user(id, body)
        print("The response of UserApi->frontier_service_enable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_enable_user: %s\n" % e)
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

# **frontier_service_get_current_user**
> V1beta1GetCurrentUserResponse frontier_service_get_current_user()

Get current user

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_current_user_response import V1beta1GetCurrentUserResponse
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
    api_instance = frontier_api.UserApi(api_client)

    try:
        # Get current user
        api_response = api_instance.frontier_service_get_current_user()
        print("The response of UserApi->frontier_service_get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_get_current_user: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1GetCurrentUserResponse**](V1beta1GetCurrentUserResponse.md)

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

# **frontier_service_get_user**
> V1beta1GetUserResponse frontier_service_get_user(id)

Get user

Get a user by id searched over all organizations in Frontier.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_user_response import V1beta1GetUserResponse
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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get user
        api_response = api_instance.frontier_service_get_user(id)
        print("The response of UserApi->frontier_service_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_get_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1GetUserResponse**](V1beta1GetUserResponse.md)

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

# **frontier_service_list_current_user_groups**
> V1beta1ListCurrentUserGroupsResponse frontier_service_list_current_user_groups(org_id=org_id, with_permissions=with_permissions, with_member_count=with_member_count)

List my groups

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_current_user_groups_response import V1beta1ListCurrentUserGroupsResponse
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
    api_instance = frontier_api.UserApi(api_client)
    org_id = 'org_id_example' # str | org_id is optional filter over an organization (optional)
    with_permissions = ['with_permissions_example'] # List[str] |  (optional)
    with_member_count = True # bool |  (optional)

    try:
        # List my groups
        api_response = api_instance.frontier_service_list_current_user_groups(org_id=org_id, with_permissions=with_permissions, with_member_count=with_member_count)
        print("The response of UserApi->frontier_service_list_current_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_current_user_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| org_id is optional filter over an organization | [optional] 
 **with_permissions** | [**List[str]**](str.md)|  | [optional] 
 **with_member_count** | **bool**|  | [optional] 

### Return type

[**V1beta1ListCurrentUserGroupsResponse**](V1beta1ListCurrentUserGroupsResponse.md)

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

# **frontier_service_list_current_user_invitations**
> V1beta1ListCurrentUserInvitationsResponse frontier_service_list_current_user_invitations()

List user invitations

List all the invitations sent to current user.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_current_user_invitations_response import V1beta1ListCurrentUserInvitationsResponse
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
    api_instance = frontier_api.UserApi(api_client)

    try:
        # List user invitations
        api_response = api_instance.frontier_service_list_current_user_invitations()
        print("The response of UserApi->frontier_service_list_current_user_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_current_user_invitations: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListCurrentUserInvitationsResponse**](V1beta1ListCurrentUserInvitationsResponse.md)

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

# **frontier_service_list_organizations_by_current_user**
> V1beta1ListOrganizationsByCurrentUserResponse frontier_service_list_organizations_by_current_user(state=state)

Get my organizations

This API returns two list of organizations for the current logged in user. i) The list of orgs which the current user is already a part of ii) The list of organizations the user can join directly (based on domain whitelisted and verified by the org). This list will also contain orgs of which user is already a part of. Note: the domain needs to be verified by the org before the it is returned as one of the joinable orgs by domain

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organizations_by_current_user_response import V1beta1ListOrganizationsByCurrentUserResponse
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
    api_instance = frontier_api.UserApi(api_client)
    state = 'state_example' # str |  (optional)

    try:
        # Get my organizations
        api_response = api_instance.frontier_service_list_organizations_by_current_user(state=state)
        print("The response of UserApi->frontier_service_list_organizations_by_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_organizations_by_current_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | [optional] 

### Return type

[**V1beta1ListOrganizationsByCurrentUserResponse**](V1beta1ListOrganizationsByCurrentUserResponse.md)

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

# **frontier_service_list_organizations_by_user**
> V1beta1ListOrganizationsByUserResponse frontier_service_list_organizations_by_user(id)

Get user organizations

This API returns two list of organizations for the user. i) The list of orgs which the current user is already a part of ii) The list of organizations the user can join directly (based on domain whitelisted and verified by the org). This list will also contain orgs of which user is already a part of. Note: the domain needs to be verified by the org before the it is returned as one of the joinable orgs by domain

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organizations_by_user_response import V1beta1ListOrganizationsByUserResponse
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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get user organizations
        api_response = api_instance.frontier_service_list_organizations_by_user(id)
        print("The response of UserApi->frontier_service_list_organizations_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_organizations_by_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListOrganizationsByUserResponse**](V1beta1ListOrganizationsByUserResponse.md)

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

# **frontier_service_list_projects_by_current_user**
> V1beta1ListProjectsByCurrentUserResponse frontier_service_list_projects_by_current_user(org_id=org_id, with_permissions=with_permissions, non_inherited=non_inherited, with_member_count=with_member_count)

Get my projects

Get all projects the current user belongs to

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_projects_by_current_user_response import V1beta1ListProjectsByCurrentUserResponse
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
    api_instance = frontier_api.UserApi(api_client)
    org_id = 'org_id_example' # str | org_id is optional and filter projects by org (optional)
    with_permissions = ['with_permissions_example'] # List[str] | list of permissions needs to be checked against each project  query params are set as with_permissions=get&with_permissions=delete to be represented as array (optional)
    non_inherited = True # bool | Note: this is a bad design and would recommend against using this filter It is used to list only projects which are explicitly given permission to user. A user could get permission to access a project either via getting access from organization level role or a group. But for some reason we want only users who could have inherited these permissions from top but we only want explictly added ones. (optional)
    with_member_count = True # bool |  (optional)

    try:
        # Get my projects
        api_response = api_instance.frontier_service_list_projects_by_current_user(org_id=org_id, with_permissions=with_permissions, non_inherited=non_inherited, with_member_count=with_member_count)
        print("The response of UserApi->frontier_service_list_projects_by_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_projects_by_current_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| org_id is optional and filter projects by org | [optional] 
 **with_permissions** | [**List[str]**](str.md)| list of permissions needs to be checked against each project  query params are set as with_permissions&#x3D;get&amp;with_permissions&#x3D;delete to be represented as array | [optional] 
 **non_inherited** | **bool**| Note: this is a bad design and would recommend against using this filter It is used to list only projects which are explicitly given permission to user. A user could get permission to access a project either via getting access from organization level role or a group. But for some reason we want only users who could have inherited these permissions from top but we only want explictly added ones. | [optional] 
 **with_member_count** | **bool**|  | [optional] 

### Return type

[**V1beta1ListProjectsByCurrentUserResponse**](V1beta1ListProjectsByCurrentUserResponse.md)

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

# **frontier_service_list_projects_by_user**
> V1beta1ListProjectsByUserResponse frontier_service_list_projects_by_user(id)

Get user projects

Get all the projects a user belongs to.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_projects_by_user_response import V1beta1ListProjectsByUserResponse
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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get user projects
        api_response = api_instance.frontier_service_list_projects_by_user(id)
        print("The response of UserApi->frontier_service_list_projects_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_projects_by_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListProjectsByUserResponse**](V1beta1ListProjectsByUserResponse.md)

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

# **frontier_service_list_user_groups**
> V1beta1ListUserGroupsResponse frontier_service_list_user_groups(id, org_id=org_id)

List user groups

Lists all the groups a user belongs to across all organization in Frontier. To get the groups of a user in a specific organization, use the org_id filter in the query parameter.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_user_groups_response import V1beta1ListUserGroupsResponse
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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | The unique ID of the user to get groups for.
    org_id = 'org_id_example' # str | The organization ID to filter groups by. If not provided, groups from all organizations are returned. (optional)

    try:
        # List user groups
        api_response = api_instance.frontier_service_list_user_groups(id, org_id=org_id)
        print("The response of UserApi->frontier_service_list_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_user_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the user to get groups for. | 
 **org_id** | **str**| The organization ID to filter groups by. If not provided, groups from all organizations are returned. | [optional] 

### Return type

[**V1beta1ListUserGroupsResponse**](V1beta1ListUserGroupsResponse.md)

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

# **frontier_service_list_user_invitations**
> V1beta1ListUserInvitationsResponse frontier_service_list_user_invitations(id)

List user invitations

List all the invitations sent to a user.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_user_invitations_response import V1beta1ListUserInvitationsResponse
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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | The user email to list the invitations for.

    try:
        # List user invitations
        api_response = api_instance.frontier_service_list_user_invitations(id)
        print("The response of UserApi->frontier_service_list_user_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_user_invitations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user email to list the invitations for. | 

### Return type

[**V1beta1ListUserInvitationsResponse**](V1beta1ListUserInvitationsResponse.md)

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

# **frontier_service_list_users**
> V1beta1ListUsersResponse frontier_service_list_users(page_size=page_size, page_num=page_num, keyword=keyword, org_id=org_id, group_id=group_id, state=state)

List public users

Returns the users from all the organizations in a Frontier instance. It can be filtered by keyword, organization, group and state. Additionally you can include page number and page size for pagination.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_users_response import V1beta1ListUsersResponse
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
    api_instance = frontier_api.UserApi(api_client)
    page_size = 56 # int | The maximum number of users to return per page. The default is 50. (optional)
    page_num = 56 # int | The page number to return. The default is 1. (optional)
    keyword = 'keyword_example' # str | The keyword to search for in name or email. (optional)
    org_id = 'org_id_example' # str | The organization ID to filter users by. (optional)
    group_id = 'group_id_example' # str | The group id to filter by. (optional)
    state = 'state_example' # str | The state to filter by. It can be enabled or disabled. (optional)

    try:
        # List public users
        api_response = api_instance.frontier_service_list_users(page_size=page_size, page_num=page_num, keyword=keyword, org_id=org_id, group_id=group_id, state=state)
        print("The response of UserApi->frontier_service_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_list_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The maximum number of users to return per page. The default is 50. | [optional] 
 **page_num** | **int**| The page number to return. The default is 1. | [optional] 
 **keyword** | **str**| The keyword to search for in name or email. | [optional] 
 **org_id** | **str**| The organization ID to filter users by. | [optional] 
 **group_id** | **str**| The group id to filter by. | [optional] 
 **state** | **str**| The state to filter by. It can be enabled or disabled. | [optional] 

### Return type

[**V1beta1ListUsersResponse**](V1beta1ListUsersResponse.md)

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

# **frontier_service_update_current_user**
> V1beta1UpdateCurrentUserResponse frontier_service_update_current_user(body)

Update current user

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_update_current_user_response import V1beta1UpdateCurrentUserResponse
from frontier_api.models.v1beta1_user_request_body import V1beta1UserRequestBody
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
    api_instance = frontier_api.UserApi(api_client)
    body = frontier_api.V1beta1UserRequestBody() # V1beta1UserRequestBody | 

    try:
        # Update current user
        api_response = api_instance.frontier_service_update_current_user(body)
        print("The response of UserApi->frontier_service_update_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_update_current_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1UserRequestBody**](V1beta1UserRequestBody.md)|  | 

### Return type

[**V1beta1UpdateCurrentUserResponse**](V1beta1UpdateCurrentUserResponse.md)

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

# **frontier_service_update_user**
> V1beta1UpdateUserResponse frontier_service_update_user(id, body)

Update user

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_update_user_response import V1beta1UpdateUserResponse
from frontier_api.models.v1beta1_user_request_body import V1beta1UserRequestBody
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
    api_instance = frontier_api.UserApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.V1beta1UserRequestBody() # V1beta1UserRequestBody | 

    try:
        # Update user
        api_response = api_instance.frontier_service_update_user(id, body)
        print("The response of UserApi->frontier_service_update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->frontier_service_update_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**V1beta1UserRequestBody**](V1beta1UserRequestBody.md)|  | 

### Return type

[**V1beta1UpdateUserResponse**](V1beta1UpdateUserResponse.md)

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

