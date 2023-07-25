<a id="__pageTop"></a>
# shield_api.apis.tags.permission_api.PermissionApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_create_permission**](#admin_service_create_permission) | **post** /v1beta1/permissions | Create platform permission
[**admin_service_delete_permission**](#admin_service_delete_permission) | **delete** /v1beta1/permissions/{id} | Delete platform permission
[**admin_service_update_permission**](#admin_service_update_permission) | **put** /v1beta1/permissions/{id} | Update platform permission
[**shield_service_get_permission**](#shield_service_get_permission) | **get** /v1beta1/permissions/{id} | Get permission
[**shield_service_list_permissions**](#shield_service_list_permissions) | **get** /v1beta1/permissions | Get all permissions

# **admin_service_create_permission**
<a id="admin_service_create_permission"></a>
> V1beta1CreatePermissionResponse admin_service_create_permission(body)

Create platform permission

Creates a permission. It can be used to grant permissions to all the resources in a Shield instance.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import permission_api
from shield_api.model.v1beta1_create_permission_response import V1beta1CreatePermissionResponse
from shield_api.model.v1beta1_create_permission_request import V1beta1CreatePermissionRequest
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
    api_instance = permission_api.PermissionApi(api_client)

    # example passing only required values which don't have defaults set
    body = V1beta1CreatePermissionRequest(
        bodies=[
            V1beta1PermissionRequestBody(
                name="name_example",
                namespace="namespace_example",
                metadata=dict(),
                title="title_example",
                key="compute.instance.get",
            )
        ],
    )
    try:
        # Create platform permission
        api_response = api_instance.admin_service_create_permission(
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling PermissionApi->admin_service_create_permission: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CreatePermissionRequest**](../../models/V1beta1CreatePermissionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#admin_service_create_permission.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#admin_service_create_permission.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#admin_service_create_permission.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#admin_service_create_permission.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#admin_service_create_permission.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#admin_service_create_permission.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#admin_service_create_permission.ApiResponseForDefault) | An unexpected error response.

#### admin_service_create_permission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CreatePermissionResponse**](../../models/V1beta1CreatePermissionResponse.md) |  | 


#### admin_service_create_permission.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_create_permission.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_create_permission.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_create_permission.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_create_permission.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_create_permission.ApiResponseForDefault
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

# **admin_service_delete_permission**
<a id="admin_service_delete_permission"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} admin_service_delete_permission(id)

Delete platform permission

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import permission_api
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
    api_instance = permission_api.PermissionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete platform permission
        api_response = api_instance.admin_service_delete_permission(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling PermissionApi->admin_service_delete_permission: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#admin_service_delete_permission.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#admin_service_delete_permission.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#admin_service_delete_permission.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#admin_service_delete_permission.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#admin_service_delete_permission.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#admin_service_delete_permission.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#admin_service_delete_permission.ApiResponseForDefault) | An unexpected error response.

#### admin_service_delete_permission.ApiResponseFor200
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

#### admin_service_delete_permission.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_delete_permission.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_delete_permission.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_delete_permission.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_delete_permission.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_delete_permission.ApiResponseForDefault
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

# **admin_service_update_permission**
<a id="admin_service_update_permission"></a>
> V1beta1UpdatePermissionResponse admin_service_update_permission(idbody)

Update platform permission

Updates a permission by ID. It can be used to grant permissions to all the resources in a Shield instance.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import permission_api
from shield_api.model.v1beta1_permission_request_body import V1beta1PermissionRequestBody
from shield_api.model.v1beta1_update_permission_response import V1beta1UpdatePermissionResponse
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
    api_instance = permission_api.PermissionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = V1beta1PermissionRequestBody(
        name="name_example",
        namespace="namespace_example",
        metadata=dict(),
        title="title_example",
        key="compute.instance.get",
    )
    try:
        # Update platform permission
        api_response = api_instance.admin_service_update_permission(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling PermissionApi->admin_service_update_permission: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PermissionRequestBody**](../../models/V1beta1PermissionRequestBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#admin_service_update_permission.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#admin_service_update_permission.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#admin_service_update_permission.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#admin_service_update_permission.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#admin_service_update_permission.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#admin_service_update_permission.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#admin_service_update_permission.ApiResponseForDefault) | An unexpected error response.

#### admin_service_update_permission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1UpdatePermissionResponse**](../../models/V1beta1UpdatePermissionResponse.md) |  | 


#### admin_service_update_permission.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_update_permission.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_update_permission.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_update_permission.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_update_permission.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_update_permission.ApiResponseForDefault
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

# **shield_service_get_permission**
<a id="shield_service_get_permission"></a>
> V1beta1GetPermissionResponse shield_service_get_permission(id)

Get permission

Returns a permission by ID

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import permission_api
from shield_api.model.rpc_status import RpcStatus
from shield_api.model.v1beta1_get_permission_response import V1beta1GetPermissionResponse
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
    api_instance = permission_api.PermissionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get permission
        api_response = api_instance.shield_service_get_permission(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling PermissionApi->shield_service_get_permission: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_get_permission.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_get_permission.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_get_permission.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_get_permission.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_get_permission.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_get_permission.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_get_permission.ApiResponseForDefault) | An unexpected error response.

#### shield_service_get_permission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1GetPermissionResponse**](../../models/V1beta1GetPermissionResponse.md) |  | 


#### shield_service_get_permission.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_permission.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_permission.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_permission.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_permission.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_permission.ApiResponseForDefault
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

# **shield_service_list_permissions**
<a id="shield_service_list_permissions"></a>
> V1beta1ListPermissionsResponse shield_service_list_permissions()

Get all permissions

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import permission_api
from shield_api.model.v1beta1_list_permissions_response import V1beta1ListPermissionsResponse
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
    api_instance = permission_api.PermissionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all permissions
        api_response = api_instance.shield_service_list_permissions()
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling PermissionApi->shield_service_list_permissions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_list_permissions.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_list_permissions.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_list_permissions.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_list_permissions.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_list_permissions.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_list_permissions.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_list_permissions.ApiResponseForDefault) | An unexpected error response.

#### shield_service_list_permissions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1ListPermissionsResponse**](../../models/V1beta1ListPermissionsResponse.md) |  | 


#### shield_service_list_permissions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_permissions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_permissions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_permissions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_permissions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_permissions.ApiResponseForDefault
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

