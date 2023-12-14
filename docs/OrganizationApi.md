# frontier_api.OrganizationApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_list_all_organizations**](OrganizationApi.md#admin_service_list_all_organizations) | **GET** /v1beta1/admin/organizations | List all organizations
[**frontier_service_accept_organization_invitation**](OrganizationApi.md#frontier_service_accept_organization_invitation) | **POST** /v1beta1/organizations/{orgId}/invitations/{id}/accept | Accept pending invitation
[**frontier_service_add_organization_users**](OrganizationApi.md#frontier_service_add_organization_users) | **POST** /v1beta1/organizations/{id}/users | Add organization user
[**frontier_service_create_organization**](OrganizationApi.md#frontier_service_create_organization) | **POST** /v1beta1/organizations | Create organization
[**frontier_service_create_organization_domain**](OrganizationApi.md#frontier_service_create_organization_domain) | **POST** /v1beta1/organizations/{orgId}/domains | Create org domain
[**frontier_service_create_organization_invitation**](OrganizationApi.md#frontier_service_create_organization_invitation) | **POST** /v1beta1/organizations/{orgId}/invitations | Invite user
[**frontier_service_delete_organization**](OrganizationApi.md#frontier_service_delete_organization) | **DELETE** /v1beta1/organizations/{id} | Delete organization
[**frontier_service_delete_organization_domain**](OrganizationApi.md#frontier_service_delete_organization_domain) | **DELETE** /v1beta1/organizations/{orgId}/domains/{id} | Delete org domain
[**frontier_service_delete_organization_invitation**](OrganizationApi.md#frontier_service_delete_organization_invitation) | **DELETE** /v1beta1/organizations/{orgId}/invitations/{id} | Delete pending invitation
[**frontier_service_disable_organization**](OrganizationApi.md#frontier_service_disable_organization) | **POST** /v1beta1/organizations/{id}/disable | Disable organization
[**frontier_service_enable_organization**](OrganizationApi.md#frontier_service_enable_organization) | **POST** /v1beta1/organizations/{id}/enable | Enable organization
[**frontier_service_get_organization**](OrganizationApi.md#frontier_service_get_organization) | **GET** /v1beta1/organizations/{id} | Get organization
[**frontier_service_get_organization_domain**](OrganizationApi.md#frontier_service_get_organization_domain) | **GET** /v1beta1/organizations/{orgId}/domains/{id} | Get org domain
[**frontier_service_get_organization_invitation**](OrganizationApi.md#frontier_service_get_organization_invitation) | **GET** /v1beta1/organizations/{orgId}/invitations/{id} | Get pending invitation
[**frontier_service_join_organization**](OrganizationApi.md#frontier_service_join_organization) | **POST** /v1beta1/organizations/{orgId}/join | Join organization
[**frontier_service_list_organization_admins**](OrganizationApi.md#frontier_service_list_organization_admins) | **GET** /v1beta1/organizations/{id}/admins | List organization admins
[**frontier_service_list_organization_domains**](OrganizationApi.md#frontier_service_list_organization_domains) | **GET** /v1beta1/organizations/{orgId}/domains | List org domains
[**frontier_service_list_organization_invitations**](OrganizationApi.md#frontier_service_list_organization_invitations) | **GET** /v1beta1/organizations/{orgId}/invitations | List pending invitations
[**frontier_service_list_organization_projects**](OrganizationApi.md#frontier_service_list_organization_projects) | **GET** /v1beta1/organizations/{id}/projects | Get organization projects
[**frontier_service_list_organization_service_users**](OrganizationApi.md#frontier_service_list_organization_service_users) | **GET** /v1beta1/organizations/{id}/serviceusers | List organization service users
[**frontier_service_list_organization_users**](OrganizationApi.md#frontier_service_list_organization_users) | **GET** /v1beta1/organizations/{id}/users | List organization users
[**frontier_service_list_organizations**](OrganizationApi.md#frontier_service_list_organizations) | **GET** /v1beta1/organizations | List organizations
[**frontier_service_remove_organization_user**](OrganizationApi.md#frontier_service_remove_organization_user) | **DELETE** /v1beta1/organizations/{id}/users/{userId} | Remove organization user
[**frontier_service_update_organization**](OrganizationApi.md#frontier_service_update_organization) | **PUT** /v1beta1/organizations/{id} | Update organization
[**frontier_service_verify_organization_domain**](OrganizationApi.md#frontier_service_verify_organization_domain) | **POST** /v1beta1/organizations/{orgId}/domains/{id}/verify | Verify org domain


# **admin_service_list_all_organizations**
> V1beta1ListAllOrganizationsResponse admin_service_list_all_organizations(user_id=user_id, state=state)

List all organizations

Lists all the organizations in a Frontier instance. It can be filtered by user and state.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_all_organizations_response import V1beta1ListAllOrganizationsResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    user_id = 'user_id_example' # str | The user id to filter by. (optional)
    state = 'state_example' # str | The state to filter by. It can be enabled or disabled. (optional)

    try:
        # List all organizations
        api_response = api_instance.admin_service_list_all_organizations(user_id=user_id, state=state)
        print("The response of OrganizationApi->admin_service_list_all_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->admin_service_list_all_organizations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id to filter by. | [optional] 
 **state** | **str**| The state to filter by. It can be enabled or disabled. | [optional] 

### Return type

[**V1beta1ListAllOrganizationsResponse**](V1beta1ListAllOrganizationsResponse.md)

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

# **frontier_service_accept_organization_invitation**
> object frontier_service_accept_organization_invitation(org_id, id)

Accept pending invitation

Accept pending invitation queued for an organization. The user will be added to the organization and groups defined in the invitation

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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Accept pending invitation
        api_response = api_instance.frontier_service_accept_organization_invitation(org_id, id)
        print("The response of OrganizationApi->frontier_service_accept_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_accept_organization_invitation: %s\n" % e)
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

# **frontier_service_add_organization_users**
> object frontier_service_add_organization_users(id, body)

Add organization user

Add a user to an organization. A user must exists in Frontier before adding it to an org. This request will fail if the user doesn't exists

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_add_organization_users_request import FrontierServiceAddOrganizationUsersRequest
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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.FrontierServiceAddOrganizationUsersRequest() # FrontierServiceAddOrganizationUsersRequest | 

    try:
        # Add organization user
        api_response = api_instance.frontier_service_add_organization_users(id, body)
        print("The response of OrganizationApi->frontier_service_add_organization_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_add_organization_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**FrontierServiceAddOrganizationUsersRequest**](FrontierServiceAddOrganizationUsersRequest.md)|  | 

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

# **frontier_service_create_organization**
> V1beta1CreateOrganizationResponse frontier_service_create_organization(body)

Create organization

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_organization_response import V1beta1CreateOrganizationResponse
from frontier_api.models.v1beta1_organization_request_body import V1beta1OrganizationRequestBody
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
    api_instance = frontier_api.OrganizationApi(api_client)
    body = frontier_api.V1beta1OrganizationRequestBody() # V1beta1OrganizationRequestBody | 

    try:
        # Create organization
        api_response = api_instance.frontier_service_create_organization(body)
        print("The response of OrganizationApi->frontier_service_create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_create_organization: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1OrganizationRequestBody**](V1beta1OrganizationRequestBody.md)|  | 

### Return type

[**V1beta1CreateOrganizationResponse**](V1beta1CreateOrganizationResponse.md)

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

# **frontier_service_create_organization_domain**
> V1beta1CreateOrganizationDomainResponse frontier_service_create_organization_domain(org_id, body)

Create org domain

Add a domain to an organization which if verified allows all users of the same domain to be signed up to the organization without invitation. This API generates a verification token for a domain which must be added to your domain's DNS provider as a TXT record should be verified with Frontier VerifyOrganizationDomain API before it can be used as an Organization's trusted domain to sign up users.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_organization_domain_request import FrontierServiceCreateOrganizationDomainRequest
from frontier_api.models.v1beta1_create_organization_domain_response import V1beta1CreateOrganizationDomainResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | unique id of the organization for which whitelisted domains are to be added
    body = frontier_api.FrontierServiceCreateOrganizationDomainRequest() # FrontierServiceCreateOrganizationDomainRequest | 

    try:
        # Create org domain
        api_response = api_instance.frontier_service_create_organization_domain(org_id, body)
        print("The response of OrganizationApi->frontier_service_create_organization_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_create_organization_domain: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| unique id of the organization for which whitelisted domains are to be added | 
 **body** | [**FrontierServiceCreateOrganizationDomainRequest**](FrontierServiceCreateOrganizationDomainRequest.md)|  | 

### Return type

[**V1beta1CreateOrganizationDomainResponse**](V1beta1CreateOrganizationDomainResponse.md)

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

# **frontier_service_create_organization_invitation**
> V1beta1CreateOrganizationInvitationResponse frontier_service_create_organization_invitation(org_id, body)

Invite user

Invite users to an organization, if user is not registered on the platform, it will be notified. Invitations expire in 7 days

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_organization_invitation_request import FrontierServiceCreateOrganizationInvitationRequest
from frontier_api.models.v1beta1_create_organization_invitation_response import V1beta1CreateOrganizationInvitationResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | unique id of the organization to which user is invited
    body = frontier_api.FrontierServiceCreateOrganizationInvitationRequest() # FrontierServiceCreateOrganizationInvitationRequest | 

    try:
        # Invite user
        api_response = api_instance.frontier_service_create_organization_invitation(org_id, body)
        print("The response of OrganizationApi->frontier_service_create_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_create_organization_invitation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| unique id of the organization to which user is invited | 
 **body** | [**FrontierServiceCreateOrganizationInvitationRequest**](FrontierServiceCreateOrganizationInvitationRequest.md)|  | 

### Return type

[**V1beta1CreateOrganizationInvitationResponse**](V1beta1CreateOrganizationInvitationResponse.md)

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

# **frontier_service_delete_organization**
> object frontier_service_delete_organization(id)

Delete organization

Delete an organization and all of its relations permanently. The organization users will not be deleted from Frontier.

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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete organization
        api_response = api_instance.frontier_service_delete_organization(id)
        print("The response of OrganizationApi->frontier_service_delete_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_delete_organization: %s\n" % e)
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

# **frontier_service_delete_organization_domain**
> object frontier_service_delete_organization_domain(org_id, id)

Delete org domain

Remove a domain from the list of an organization's trusted domains list

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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | unique id of the organization for which whitelisted domains are to be deleted
    id = 'id_example' # str | unique id of the domain to be deleted

    try:
        # Delete org domain
        api_response = api_instance.frontier_service_delete_organization_domain(org_id, id)
        print("The response of OrganizationApi->frontier_service_delete_organization_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_delete_organization_domain: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| unique id of the organization for which whitelisted domains are to be deleted | 
 **id** | **str**| unique id of the domain to be deleted | 

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

# **frontier_service_delete_organization_invitation**
> object frontier_service_delete_organization_invitation(org_id, id)

Delete pending invitation

Delete a pending invitation queued for an organization

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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Delete pending invitation
        api_response = api_instance.frontier_service_delete_organization_invitation(org_id, id)
        print("The response of OrganizationApi->frontier_service_delete_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_delete_organization_invitation: %s\n" % e)
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

# **frontier_service_disable_organization**
> object frontier_service_disable_organization(id, body)

Disable organization

Sets the state of the organization as disabled. The existing users in the org will not be able to access any organization resources.

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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Disable organization
        api_response = api_instance.frontier_service_disable_organization(id, body)
        print("The response of OrganizationApi->frontier_service_disable_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_disable_organization: %s\n" % e)
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

# **frontier_service_enable_organization**
> object frontier_service_enable_organization(id, body)

Enable organization

Sets the state of the organization as enabled. The existing users in the org will be able to access any organization resources.

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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Enable organization
        api_response = api_instance.frontier_service_enable_organization(id, body)
        print("The response of OrganizationApi->frontier_service_enable_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_enable_organization: %s\n" % e)
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

# **frontier_service_get_organization**
> V1beta1GetOrganizationResponse frontier_service_get_organization(id)

Get organization

Get organization by ID or name

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_organization_response import V1beta1GetOrganizationResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get organization
        api_response = api_instance.frontier_service_get_organization(id)
        print("The response of OrganizationApi->frontier_service_get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_get_organization: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1GetOrganizationResponse**](V1beta1GetOrganizationResponse.md)

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

# **frontier_service_get_organization_domain**
> V1beta1GetOrganizationDomainResponse frontier_service_get_organization_domain(org_id, id)

Get org domain

Get a domain from the list of an organization's whitelisted domains. Returns both verified and unverified domains by their ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_organization_domain_response import V1beta1GetOrganizationDomainResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | unique id of the organization for which whitelisted domain is to be retrieved
    id = 'id_example' # str | unique id of the domain to be retrieved

    try:
        # Get org domain
        api_response = api_instance.frontier_service_get_organization_domain(org_id, id)
        print("The response of OrganizationApi->frontier_service_get_organization_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_get_organization_domain: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| unique id of the organization for which whitelisted domain is to be retrieved | 
 **id** | **str**| unique id of the domain to be retrieved | 

### Return type

[**V1beta1GetOrganizationDomainResponse**](V1beta1GetOrganizationDomainResponse.md)

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

# **frontier_service_get_organization_invitation**
> V1beta1GetOrganizationInvitationResponse frontier_service_get_organization_invitation(org_id, id)

Get pending invitation

Returns a pending invitation queued for an organization

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_organization_invitation_response import V1beta1GetOrganizationInvitationResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Get pending invitation
        api_response = api_instance.frontier_service_get_organization_invitation(org_id, id)
        print("The response of OrganizationApi->frontier_service_get_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_get_organization_invitation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**V1beta1GetOrganizationInvitationResponse**](V1beta1GetOrganizationInvitationResponse.md)

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

# **frontier_service_join_organization**
> object frontier_service_join_organization(org_id)

Join organization

Allows the current logged in user to join the Org if one is not a part of it. The user will only be able to join when the user email's domain matches the organization's whitelisted domains.

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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Join organization
        api_response = api_instance.frontier_service_join_organization(org_id)
        print("The response of OrganizationApi->frontier_service_join_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_join_organization: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

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

# **frontier_service_list_organization_admins**
> V1beta1ListOrganizationAdminsResponse frontier_service_list_organization_admins(id)

List organization admins

Returns a list admins of an organization

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_admins_response import V1beta1ListOrganizationAdminsResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # List organization admins
        api_response = api_instance.frontier_service_list_organization_admins(id)
        print("The response of OrganizationApi->frontier_service_list_organization_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_list_organization_admins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListOrganizationAdminsResponse**](V1beta1ListOrganizationAdminsResponse.md)

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

# **frontier_service_list_organization_domains**
> V1beta1ListOrganizationDomainsResponse frontier_service_list_organization_domains(org_id, state=state)

List org domains

Returns all domains whitelisted for an organization (both pending and verified if no filters are provided for the state). The verified domains allow users email with the org's whitelisted domain to join the organization without invitation.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_domains_response import V1beta1ListOrganizationDomainsResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | unique id of the organization for which whitelisted domains are to be listed
    state = 'state_example' # str | filter to list domains by their state (pending/verified). If not provided, all domains for an org will be listed (optional)

    try:
        # List org domains
        api_response = api_instance.frontier_service_list_organization_domains(org_id, state=state)
        print("The response of OrganizationApi->frontier_service_list_organization_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_list_organization_domains: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| unique id of the organization for which whitelisted domains are to be listed | 
 **state** | **str**| filter to list domains by their state (pending/verified). If not provided, all domains for an org will be listed | [optional] 

### Return type

[**V1beta1ListOrganizationDomainsResponse**](V1beta1ListOrganizationDomainsResponse.md)

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

# **frontier_service_list_organization_invitations**
> V1beta1ListOrganizationInvitationsResponse frontier_service_list_organization_invitations(org_id, user_id=user_id)

List pending invitations

Returns all pending invitations queued for an organization

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_invitations_response import V1beta1ListOrganizationInvitationsResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | unique id of the organization to which user is invited
    user_id = 'user_id_example' # str | user_id filter is the email id of user who are invited inside the organization. (optional)

    try:
        # List pending invitations
        api_response = api_instance.frontier_service_list_organization_invitations(org_id, user_id=user_id)
        print("The response of OrganizationApi->frontier_service_list_organization_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_list_organization_invitations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| unique id of the organization to which user is invited | 
 **user_id** | **str**| user_id filter is the email id of user who are invited inside the organization. | [optional] 

### Return type

[**V1beta1ListOrganizationInvitationsResponse**](V1beta1ListOrganizationInvitationsResponse.md)

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

# **frontier_service_list_organization_projects**
> V1beta1ListOrganizationProjectsResponse frontier_service_list_organization_projects(id, state=state)

Get organization projects

Get all projects that belong to an organization

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_projects_response import V1beta1ListOrganizationProjectsResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 
    state = 'state_example' # str | Filter projects by state. If not specified, all projects are returned. <br/> *Possible values:* `enabled` or `disabled` (optional)

    try:
        # Get organization projects
        api_response = api_instance.frontier_service_list_organization_projects(id, state=state)
        print("The response of OrganizationApi->frontier_service_list_organization_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_list_organization_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **state** | **str**| Filter projects by state. If not specified, all projects are returned. &lt;br/&gt; *Possible values:* &#x60;enabled&#x60; or &#x60;disabled&#x60; | [optional] 

### Return type

[**V1beta1ListOrganizationProjectsResponse**](V1beta1ListOrganizationProjectsResponse.md)

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

# **frontier_service_list_organization_service_users**
> V1beta1ListOrganizationServiceUsersResponse frontier_service_list_organization_service_users(id)

List organization service users

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_service_users_response import V1beta1ListOrganizationServiceUsersResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # List organization service users
        api_response = api_instance.frontier_service_list_organization_service_users(id)
        print("The response of OrganizationApi->frontier_service_list_organization_service_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_list_organization_service_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1ListOrganizationServiceUsersResponse**](V1beta1ListOrganizationServiceUsersResponse.md)

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

# **frontier_service_list_organization_users**
> V1beta1ListOrganizationUsersResponse frontier_service_list_organization_users(id, permission_filter=permission_filter, with_roles=with_roles)

List organization users

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_users_response import V1beta1ListOrganizationUsersResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 
    permission_filter = 'permission_filter_example' # str |  (optional)
    with_roles = True # bool |  (optional)

    try:
        # List organization users
        api_response = api_instance.frontier_service_list_organization_users(id, permission_filter=permission_filter, with_roles=with_roles)
        print("The response of OrganizationApi->frontier_service_list_organization_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_list_organization_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **permission_filter** | **str**|  | [optional] 
 **with_roles** | **bool**|  | [optional] 

### Return type

[**V1beta1ListOrganizationUsersResponse**](V1beta1ListOrganizationUsersResponse.md)

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

# **frontier_service_list_organizations**
> V1beta1ListOrganizationsResponse frontier_service_list_organizations(user_id=user_id, state=state)

List organizations

Returns a list of organizations. It can be filtered by userID or organization state.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organizations_response import V1beta1ListOrganizationsResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    user_id = 'user_id_example' # str | The user ID to filter by. It can be used to list all the organizations that the user is a member of. Otherwise, all the organizations in the Frontier instance will be listed. (optional)
    state = 'state_example' # str | The state to filter by. It can be `enabled` or `disabled`. (optional)

    try:
        # List organizations
        api_response = api_instance.frontier_service_list_organizations(user_id=user_id, state=state)
        print("The response of OrganizationApi->frontier_service_list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_list_organizations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID to filter by. It can be used to list all the organizations that the user is a member of. Otherwise, all the organizations in the Frontier instance will be listed. | [optional] 
 **state** | **str**| The state to filter by. It can be &#x60;enabled&#x60; or &#x60;disabled&#x60;. | [optional] 

### Return type

[**V1beta1ListOrganizationsResponse**](V1beta1ListOrganizationsResponse.md)

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

# **frontier_service_remove_organization_user**
> object frontier_service_remove_organization_user(id, user_id)

Remove organization user

Remove a user from an organization

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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove organization user
        api_response = api_instance.frontier_service_remove_organization_user(id, user_id)
        print("The response of OrganizationApi->frontier_service_remove_organization_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_remove_organization_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **frontier_service_update_organization**
> V1beta1UpdateOrganizationResponse frontier_service_update_organization(id, body)

Update organization

Update organization by ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_organization_request_body import V1beta1OrganizationRequestBody
from frontier_api.models.v1beta1_update_organization_response import V1beta1UpdateOrganizationResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.V1beta1OrganizationRequestBody() # V1beta1OrganizationRequestBody | 

    try:
        # Update organization
        api_response = api_instance.frontier_service_update_organization(id, body)
        print("The response of OrganizationApi->frontier_service_update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_update_organization: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**V1beta1OrganizationRequestBody**](V1beta1OrganizationRequestBody.md)|  | 

### Return type

[**V1beta1UpdateOrganizationResponse**](V1beta1UpdateOrganizationResponse.md)

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

# **frontier_service_verify_organization_domain**
> V1beta1VerifyOrganizationDomainResponse frontier_service_verify_organization_domain(org_id, id, body)

Verify org domain

Verify a domain for an organization with a verification token generated by Frontier GenerateDomainVerificationToken API. The token must be added to your domain's DNS provider as a TXT record before it can be verified. This API returns the state of the domain (pending/verified) after verification.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_verify_organization_domain_response import V1beta1VerifyOrganizationDomainResponse
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
    api_instance = frontier_api.OrganizationApi(api_client)
    org_id = 'org_id_example' # str | unique id of the organization for which whitelisted domains are to be verified
    id = 'id_example' # str | unique id of the domain to be verified
    body = None # object | 

    try:
        # Verify org domain
        api_response = api_instance.frontier_service_verify_organization_domain(org_id, id, body)
        print("The response of OrganizationApi->frontier_service_verify_organization_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->frontier_service_verify_organization_domain: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| unique id of the organization for which whitelisted domains are to be verified | 
 **id** | **str**| unique id of the domain to be verified | 
 **body** | **object**|  | 

### Return type

[**V1beta1VerifyOrganizationDomainResponse**](V1beta1VerifyOrganizationDomainResponse.md)

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

