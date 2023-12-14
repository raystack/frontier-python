# frontier_api.AuditLogApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_organization_audit_logs**](AuditLogApi.md#frontier_service_create_organization_audit_logs) | **POST** /v1beta1/organization/{orgId}/auditlogs | Create audit log
[**frontier_service_get_organization_audit_log**](AuditLogApi.md#frontier_service_get_organization_audit_log) | **GET** /v1beta1/organization/{orgId}/auditlogs/{id} | Get audit log
[**frontier_service_list_organization_audit_logs**](AuditLogApi.md#frontier_service_list_organization_audit_logs) | **GET** /v1beta1/organization/{orgId}/auditlogs | List audit logs


# **frontier_service_create_organization_audit_logs**
> object frontier_service_create_organization_audit_logs(org_id, body)

Create audit log

Create new audit logs in a batch.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_create_organization_audit_logs_request import FrontierServiceCreateOrganizationAuditLogsRequest
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
    api_instance = frontier_api.AuditLogApi(api_client)
    org_id = 'org_id_example' # str | 
    body = frontier_api.FrontierServiceCreateOrganizationAuditLogsRequest() # FrontierServiceCreateOrganizationAuditLogsRequest | 

    try:
        # Create audit log
        api_response = api_instance.frontier_service_create_organization_audit_logs(org_id, body)
        print("The response of AuditLogApi->frontier_service_create_organization_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->frontier_service_create_organization_audit_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **body** | [**FrontierServiceCreateOrganizationAuditLogsRequest**](FrontierServiceCreateOrganizationAuditLogsRequest.md)|  | 

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

# **frontier_service_get_organization_audit_log**
> V1beta1GetOrganizationAuditLogResponse frontier_service_get_organization_audit_log(org_id, id)

Get audit log

Get an audit log by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_organization_audit_log_response import V1beta1GetOrganizationAuditLogResponse
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
    api_instance = frontier_api.AuditLogApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Get audit log
        api_response = api_instance.frontier_service_get_organization_audit_log(org_id, id)
        print("The response of AuditLogApi->frontier_service_get_organization_audit_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->frontier_service_get_organization_audit_log: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**V1beta1GetOrganizationAuditLogResponse**](V1beta1GetOrganizationAuditLogResponse.md)

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

# **frontier_service_list_organization_audit_logs**
> V1beta1ListOrganizationAuditLogsResponse frontier_service_list_organization_audit_logs(org_id, source=source, action=action, start_time=start_time, end_time=end_time)

List audit logs

Returns a list of audit logs of an organization in Frontier.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_organization_audit_logs_response import V1beta1ListOrganizationAuditLogsResponse
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
    api_instance = frontier_api.AuditLogApi(api_client)
    org_id = 'org_id_example' # str | 
    source = 'source_example' # str |  (optional)
    action = 'action_example' # str |  (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | start_time and end_time are inclusive (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # List audit logs
        api_response = api_instance.frontier_service_list_organization_audit_logs(org_id, source=source, action=action, start_time=start_time, end_time=end_time)
        print("The response of AuditLogApi->frontier_service_list_organization_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->frontier_service_list_organization_audit_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **source** | **str**|  | [optional] 
 **action** | **str**|  | [optional] 
 **start_time** | **datetime**| start_time and end_time are inclusive | [optional] 
 **end_time** | **datetime**|  | [optional] 

### Return type

[**V1beta1ListOrganizationAuditLogsResponse**](V1beta1ListOrganizationAuditLogsResponse.md)

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

