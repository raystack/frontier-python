<a id="__pageTop"></a>
# shield_api.apis.tags.namespace_api.NamespaceApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shield_service_get_namespace**](#shield_service_get_namespace) | **get** /v1beta1/namespaces/{id} | Get namespace
[**shield_service_list_namespaces**](#shield_service_list_namespaces) | **get** /v1beta1/namespaces | Get all namespaces

# **shield_service_get_namespace**
<a id="shield_service_get_namespace"></a>
> V1beta1GetNamespaceResponse shield_service_get_namespace(id)

Get namespace

Returns a namespace by ID

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import namespace_api
from shield_api.model.v1beta1_get_namespace_response import V1beta1GetNamespaceResponse
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
    api_instance = namespace_api.NamespaceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get namespace
        api_response = api_instance.shield_service_get_namespace(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling NamespaceApi->shield_service_get_namespace: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_get_namespace.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_get_namespace.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_get_namespace.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_get_namespace.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_get_namespace.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_get_namespace.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_get_namespace.ApiResponseForDefault) | An unexpected error response.

#### shield_service_get_namespace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1GetNamespaceResponse**](../../models/V1beta1GetNamespaceResponse.md) |  | 


#### shield_service_get_namespace.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_namespace.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_namespace.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_namespace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_namespace.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_namespace.ApiResponseForDefault
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

# **shield_service_list_namespaces**
<a id="shield_service_list_namespaces"></a>
> V1beta1ListNamespacesResponse shield_service_list_namespaces()

Get all namespaces

Returns the list of all namespaces in a Shield instance

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import namespace_api
from shield_api.model.v1beta1_list_namespaces_response import V1beta1ListNamespacesResponse
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
    api_instance = namespace_api.NamespaceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all namespaces
        api_response = api_instance.shield_service_list_namespaces()
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling NamespaceApi->shield_service_list_namespaces: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_list_namespaces.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_list_namespaces.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_list_namespaces.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_list_namespaces.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_list_namespaces.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_list_namespaces.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_list_namespaces.ApiResponseForDefault) | An unexpected error response.

#### shield_service_list_namespaces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1ListNamespacesResponse**](../../models/V1beta1ListNamespacesResponse.md) |  | 


#### shield_service_list_namespaces.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_namespaces.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_namespaces.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_namespaces.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_namespaces.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_namespaces.ApiResponseForDefault
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

