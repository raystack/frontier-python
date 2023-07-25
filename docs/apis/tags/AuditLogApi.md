<a id="__pageTop"></a>
# shield_api.apis.tags.audit_log_api.AuditLogApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shield_service_create_organization_audit_logs**](#shield_service_create_organization_audit_logs) | **post** /v1beta1/organization/{orgId}/auditlogs | Create audit log
[**shield_service_get_organization_audit_log**](#shield_service_get_organization_audit_log) | **get** /v1beta1/organization/{orgId}/auditlogs/{id} | Get audit log
[**shield_service_list_organization_audit_logs**](#shield_service_list_organization_audit_logs) | **get** /v1beta1/organization/{orgId}/auditlogs | List audit logs

# **shield_service_create_organization_audit_logs**
<a id="shield_service_create_organization_audit_logs"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} shield_service_create_organization_audit_logs(org_idbody)

Create audit log

Create new audit logs in a batch.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import audit_log_api
from shield_api.model.v1beta1_audit_log import V1beta1AuditLog
from shield_api.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:7400
# See configuration.py for a list of all supported configuration parameters.
configuration = shield_api.Configuration(
    host = "http://127.0.0.1:7400"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = shield_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
# Enter a context with an instance of the API client
with shield_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log_api.AuditLogApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orgId': "orgId_example",
    }
    body = dict(
        logs=[
            V1beta1AuditLog(
                id="id_example",
                source="auth",
                action="action_example",
                actor=V1beta1AuditLogActor(
                    id="id_example",
                    type="type_example",
                    name="name_example",
                ),
,
                context=dict(
                    "key": "key_example",
                ),
                created_at="2023-06-07T05:39:56.961Z",
            )
        ],
    )
    try:
        # Create audit log
        api_response = api_instance.shield_service_create_organization_audit_logs(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling AuditLogApi->shield_service_create_organization_audit_logs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[logs](#logs)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# logs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1beta1AuditLog**]({{complexTypePrefix}}V1beta1AuditLog.md) | [**V1beta1AuditLog**]({{complexTypePrefix}}V1beta1AuditLog.md) | [**V1beta1AuditLog**]({{complexTypePrefix}}V1beta1AuditLog.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orgId | OrgIdSchema | | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_create_organization_audit_logs.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_create_organization_audit_logs.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_create_organization_audit_logs.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_create_organization_audit_logs.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_create_organization_audit_logs.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_create_organization_audit_logs.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_create_organization_audit_logs.ApiResponseForDefault) | An unexpected error response.

#### shield_service_create_organization_audit_logs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### shield_service_create_organization_audit_logs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_organization_audit_logs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_organization_audit_logs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_organization_audit_logs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_organization_audit_logs.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_organization_audit_logs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


### Authorization

[Basic](../../../README.md#Basic)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **shield_service_get_organization_audit_log**
<a id="shield_service_get_organization_audit_log"></a>
> V1beta1GetOrganizationAuditLogResponse shield_service_get_organization_audit_log(org_idid)

Get audit log

Get an audit log by ID.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import audit_log_api
from shield_api.model.v1beta1_get_organization_audit_log_response import V1beta1GetOrganizationAuditLogResponse
from shield_api.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:7400
# See configuration.py for a list of all supported configuration parameters.
configuration = shield_api.Configuration(
    host = "http://127.0.0.1:7400"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = shield_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
# Enter a context with an instance of the API client
with shield_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log_api.AuditLogApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orgId': "orgId_example",
        'id': "id_example",
    }
    try:
        # Get audit log
        api_response = api_instance.shield_service_get_organization_audit_log(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling AuditLogApi->shield_service_get_organization_audit_log: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orgId | OrgIdSchema | | 
id | IdSchema | | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_get_organization_audit_log.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_get_organization_audit_log.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_get_organization_audit_log.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_get_organization_audit_log.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_get_organization_audit_log.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_get_organization_audit_log.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_get_organization_audit_log.ApiResponseForDefault) | An unexpected error response.

#### shield_service_get_organization_audit_log.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1GetOrganizationAuditLogResponse**](../../models/V1beta1GetOrganizationAuditLogResponse.md) |  | 


#### shield_service_get_organization_audit_log.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_organization_audit_log.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_organization_audit_log.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_organization_audit_log.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_organization_audit_log.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_organization_audit_log.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


### Authorization

[Basic](../../../README.md#Basic)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **shield_service_list_organization_audit_logs**
<a id="shield_service_list_organization_audit_logs"></a>
> V1beta1ListOrganizationAuditLogsResponse shield_service_list_organization_audit_logs(org_id)

List audit logs

Returns a list of audit logs of an organization in Shield.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import audit_log_api
from shield_api.model.v1beta1_list_organization_audit_logs_response import V1beta1ListOrganizationAuditLogsResponse
from shield_api.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:7400
# See configuration.py for a list of all supported configuration parameters.
configuration = shield_api.Configuration(
    host = "http://127.0.0.1:7400"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = shield_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
# Enter a context with an instance of the API client
with shield_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log_api.AuditLogApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orgId': "orgId_example",
    }
    query_params = {
    }
    try:
        # List audit logs
        api_response = api_instance.shield_service_list_organization_audit_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling AuditLogApi->shield_service_list_organization_audit_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'orgId': "orgId_example",
    }
    query_params = {
        'source': "source_example",
        'action': "action_example",
        'startTime': "1970-01-01T00:00:00.00Z",
        'endTime': "1970-01-01T00:00:00.00Z",
    }
    try:
        # List audit logs
        api_response = api_instance.shield_service_list_organization_audit_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling AuditLogApi->shield_service_list_organization_audit_logs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
source | SourceSchema | | optional
action | ActionSchema | | optional
startTime | StartTimeSchema | | optional
endTime | EndTimeSchema | | optional


# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orgId | OrgIdSchema | | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_list_organization_audit_logs.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_list_organization_audit_logs.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_list_organization_audit_logs.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_list_organization_audit_logs.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_list_organization_audit_logs.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_list_organization_audit_logs.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_list_organization_audit_logs.ApiResponseForDefault) | An unexpected error response.

#### shield_service_list_organization_audit_logs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1ListOrganizationAuditLogsResponse**](../../models/V1beta1ListOrganizationAuditLogsResponse.md) |  | 


#### shield_service_list_organization_audit_logs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_organization_audit_logs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_organization_audit_logs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_organization_audit_logs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_organization_audit_logs.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_organization_audit_logs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


### Authorization

[Basic](../../../README.md#Basic)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

