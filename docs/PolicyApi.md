# frontier_api.PolicyApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_policy**](PolicyApi.md#frontier_service_create_policy) | **POST** /v1beta1/policies | Create policy
[**frontier_service_delete_policy**](PolicyApi.md#frontier_service_delete_policy) | **DELETE** /v1beta1/policies/{id} | Delete Policy
[**frontier_service_get_policy**](PolicyApi.md#frontier_service_get_policy) | **GET** /v1beta1/policies/{id} | Get policy
[**frontier_service_list_policies**](PolicyApi.md#frontier_service_list_policies) | **GET** /v1beta1/policies | List all policies
[**frontier_service_update_policy**](PolicyApi.md#frontier_service_update_policy) | **PUT** /v1beta1/policies/{id} | Update policy


# **frontier_service_create_policy**
> V1beta1CreatePolicyResponse frontier_service_create_policy(body)

Create policy

Creates a policy 

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_policy_response import V1beta1CreatePolicyResponse
from frontier_api.models.v1beta1_policy_request_body import V1beta1PolicyRequestBody
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
    api_instance = frontier_api.PolicyApi(api_client)
    body = frontier_api.V1beta1PolicyRequestBody() # V1beta1PolicyRequestBody | 

    try:
        # Create policy
        api_response = api_instance.frontier_service_create_policy(body)
        print("The response of PolicyApi->frontier_service_create_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->frontier_service_create_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1PolicyRequestBody**](V1beta1PolicyRequestBody.md)|  | 

### Return type

[**V1beta1CreatePolicyResponse**](V1beta1CreatePolicyResponse.md)

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

# **frontier_service_delete_policy**
> object frontier_service_delete_policy(id)

Delete Policy

Delete a policy all of its relations permanently.

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
    api_instance = frontier_api.PolicyApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Policy
        api_response = api_instance.frontier_service_delete_policy(id)
        print("The response of PolicyApi->frontier_service_delete_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->frontier_service_delete_policy: %s\n" % e)
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

# **frontier_service_get_policy**
> V1beta1GetPolicyResponse frontier_service_get_policy(id)

Get policy

Returns a policy by ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_policy_response import V1beta1GetPolicyResponse
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
    api_instance = frontier_api.PolicyApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get policy
        api_response = api_instance.frontier_service_get_policy(id)
        print("The response of PolicyApi->frontier_service_get_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->frontier_service_get_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1GetPolicyResponse**](V1beta1GetPolicyResponse.md)

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

# **frontier_service_list_policies**
> V1beta1ListPoliciesResponse frontier_service_list_policies(org_id=org_id, project_id=project_id, user_id=user_id, role_id=role_id, group_id=group_id)

List all policies

Lists all the policies from all the organizations in a Frontier instance. It can be filtered by organization, project, user, role and group.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_policies_response import V1beta1ListPoliciesResponse
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
    api_instance = frontier_api.PolicyApi(api_client)
    org_id = 'org_id_example' # str | The organization id to filter by. (optional)
    project_id = 'project_id_example' # str | The project id to filter by. (optional)
    user_id = 'user_id_example' # str | The user id to filter by. (optional)
    role_id = 'role_id_example' # str | The role id to filter by. (optional)
    group_id = 'group_id_example' # str | The group id to filter by. (optional)

    try:
        # List all policies
        api_response = api_instance.frontier_service_list_policies(org_id=org_id, project_id=project_id, user_id=user_id, role_id=role_id, group_id=group_id)
        print("The response of PolicyApi->frontier_service_list_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->frontier_service_list_policies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The organization id to filter by. | [optional] 
 **project_id** | **str**| The project id to filter by. | [optional] 
 **user_id** | **str**| The user id to filter by. | [optional] 
 **role_id** | **str**| The role id to filter by. | [optional] 
 **group_id** | **str**| The group id to filter by. | [optional] 

### Return type

[**V1beta1ListPoliciesResponse**](V1beta1ListPoliciesResponse.md)

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

# **frontier_service_update_policy**
> V1beta1UpdatePolicyResponse frontier_service_update_policy(id, body)

Update policy

Updates a policy by ID

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_policy_request_body import V1beta1PolicyRequestBody
from frontier_api.models.v1beta1_update_policy_response import V1beta1UpdatePolicyResponse
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
    api_instance = frontier_api.PolicyApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.V1beta1PolicyRequestBody() # V1beta1PolicyRequestBody | 

    try:
        # Update policy
        api_response = api_instance.frontier_service_update_policy(id, body)
        print("The response of PolicyApi->frontier_service_update_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->frontier_service_update_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**V1beta1PolicyRequestBody**](V1beta1PolicyRequestBody.md)|  | 

### Return type

[**V1beta1UpdatePolicyResponse**](V1beta1UpdatePolicyResponse.md)

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

