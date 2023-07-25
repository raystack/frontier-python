<a id="__pageTop"></a>
# shield_api.apis.tags.meta_schema_api.MetaSchemaApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shield_service_create_meta_schema**](#shield_service_create_meta_schema) | **post** /v1beta1/meta/schemas | Create metaschema
[**shield_service_delete_meta_schema**](#shield_service_delete_meta_schema) | **delete** /v1beta1/meta/schemas/{id} | Delete metaschema
[**shield_service_get_meta_schema**](#shield_service_get_meta_schema) | **get** /v1beta1/meta/schemas/{id} | Get metaschema
[**shield_service_list_meta_schemas**](#shield_service_list_meta_schemas) | **get** /v1beta1/meta/schemas | List metaschemas
[**shield_service_update_meta_schema**](#shield_service_update_meta_schema) | **put** /v1beta1/meta/schemas/{id} | Update metaschema

# **shield_service_create_meta_schema**
<a id="shield_service_create_meta_schema"></a>
> V1beta1CreateMetaSchemaResponse shield_service_create_meta_schema(body)

Create metaschema

Create a new metadata schema. The metaschema **name** must be unique within the entire Shield instance and can contain only alphanumeric characters, dashes and underscores. The metaschema **schema** must be a valid JSON schema.Please refer to https://json-schema.org/ to know more about json schema. <br/>*Example:* `{name:\"user\",schema:{\"type\":\"object\",\"properties\":{\"label\":{\"type\":\"object\",\"additionalProperties\":{\"type\":\"string\"}},\"description\":{\"type\":\"string\"}}}}`

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import meta_schema_api
from shield_api.model.v1beta1_meta_schema_request_body import V1beta1MetaSchemaRequestBody
from shield_api.model.v1beta1_create_meta_schema_response import V1beta1CreateMetaSchemaResponse
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
    api_instance = meta_schema_api.MetaSchemaApi(api_client)

    # example passing only required values which don't have defaults set
    body = V1beta1MetaSchemaRequestBody(
        name="name_example",
        schema="schema_example",
    )
    try:
        # Create metaschema
        api_response = api_instance.shield_service_create_meta_schema(
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling MetaSchemaApi->shield_service_create_meta_schema: %s\n" % e)
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
[**V1beta1MetaSchemaRequestBody**](../../models/V1beta1MetaSchemaRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_create_meta_schema.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_create_meta_schema.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_create_meta_schema.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_create_meta_schema.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_create_meta_schema.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_create_meta_schema.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_create_meta_schema.ApiResponseForDefault) | An unexpected error response.

#### shield_service_create_meta_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CreateMetaSchemaResponse**](../../models/V1beta1CreateMetaSchemaResponse.md) |  | 


#### shield_service_create_meta_schema.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_meta_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_meta_schema.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_meta_schema.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_meta_schema.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_meta_schema.ApiResponseForDefault
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

# **shield_service_delete_meta_schema**
<a id="shield_service_delete_meta_schema"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} shield_service_delete_meta_schema(id)

Delete metaschema

Delete a metadata schema permanently. Once deleted the metaschema won't be used to validate the metadata. For example, if a metaschema(with `label` and `description` fields) is used to validate the metadata of a user, then deleting the metaschema will not validate the metadata of the user and metadata field can contain any key-value pair(and say another field called `foo` can be inserted in a user's metadata).

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import meta_schema_api
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
    api_instance = meta_schema_api.MetaSchemaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete metaschema
        api_response = api_instance.shield_service_delete_meta_schema(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling MetaSchemaApi->shield_service_delete_meta_schema: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_delete_meta_schema.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_delete_meta_schema.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_delete_meta_schema.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_delete_meta_schema.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_delete_meta_schema.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_delete_meta_schema.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_delete_meta_schema.ApiResponseForDefault) | An unexpected error response.

#### shield_service_delete_meta_schema.ApiResponseFor200
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

#### shield_service_delete_meta_schema.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_meta_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_meta_schema.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_meta_schema.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_meta_schema.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_meta_schema.ApiResponseForDefault
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

# **shield_service_get_meta_schema**
<a id="shield_service_get_meta_schema"></a>
> V1beta1GetMetaSchemaResponse shield_service_get_meta_schema(id)

Get metaschema

Get a metadata schema by ID.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import meta_schema_api
from shield_api.model.v1beta1_get_meta_schema_response import V1beta1GetMetaSchemaResponse
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
    api_instance = meta_schema_api.MetaSchemaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get metaschema
        api_response = api_instance.shield_service_get_meta_schema(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling MetaSchemaApi->shield_service_get_meta_schema: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_get_meta_schema.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_get_meta_schema.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_get_meta_schema.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_get_meta_schema.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_get_meta_schema.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_get_meta_schema.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_get_meta_schema.ApiResponseForDefault) | An unexpected error response.

#### shield_service_get_meta_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1GetMetaSchemaResponse**](../../models/V1beta1GetMetaSchemaResponse.md) |  | 


#### shield_service_get_meta_schema.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_meta_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_meta_schema.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_meta_schema.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_meta_schema.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_meta_schema.ApiResponseForDefault
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

# **shield_service_list_meta_schemas**
<a id="shield_service_list_meta_schemas"></a>
> V1beta1ListMetaSchemasResponse shield_service_list_meta_schemas()

List metaschemas

Returns a list of all metaschemas configured on an instance level in Shield. e.g user, project, organization etc

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import meta_schema_api
from shield_api.model.v1beta1_list_meta_schemas_response import V1beta1ListMetaSchemasResponse
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
    api_instance = meta_schema_api.MetaSchemaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List metaschemas
        api_response = api_instance.shield_service_list_meta_schemas()
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling MetaSchemaApi->shield_service_list_meta_schemas: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_list_meta_schemas.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_list_meta_schemas.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_list_meta_schemas.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_list_meta_schemas.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_list_meta_schemas.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_list_meta_schemas.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_list_meta_schemas.ApiResponseForDefault) | An unexpected error response.

#### shield_service_list_meta_schemas.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1ListMetaSchemasResponse**](../../models/V1beta1ListMetaSchemasResponse.md) |  | 


#### shield_service_list_meta_schemas.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_meta_schemas.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_meta_schemas.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_meta_schemas.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_meta_schemas.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_meta_schemas.ApiResponseForDefault
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

# **shield_service_update_meta_schema**
<a id="shield_service_update_meta_schema"></a>
> V1beta1UpdateMetaSchemaResponse shield_service_update_meta_schema(idbody)

Update metaschema

Update a metadata schema. Only `schema` field of a metaschema can be updated. The metaschema `schema` must be a valid JSON schema.Please refer to https://json-schema.org/ to know more about json schema. <br/>*Example:* `{name:\"user\",schema:{\"type\":\"object\",\"properties\":{\"label\":{\"type\":\"object\",\"additionalProperties\":{\"type\":\"string\"}},\"description\":{\"type\":\"string\"}}}}`

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import meta_schema_api
from shield_api.model.v1beta1_meta_schema_request_body import V1beta1MetaSchemaRequestBody
from shield_api.model.rpc_status import RpcStatus
from shield_api.model.v1beta1_update_meta_schema_response import V1beta1UpdateMetaSchemaResponse
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
    api_instance = meta_schema_api.MetaSchemaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = V1beta1MetaSchemaRequestBody(
        name="name_example",
        schema="schema_example",
    )
    try:
        # Update metaschema
        api_response = api_instance.shield_service_update_meta_schema(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling MetaSchemaApi->shield_service_update_meta_schema: %s\n" % e)
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
[**V1beta1MetaSchemaRequestBody**](../../models/V1beta1MetaSchemaRequestBody.md) |  | 


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
200 | [ApiResponseFor200](#shield_service_update_meta_schema.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_update_meta_schema.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_update_meta_schema.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_update_meta_schema.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_update_meta_schema.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_update_meta_schema.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_update_meta_schema.ApiResponseForDefault) | An unexpected error response.

#### shield_service_update_meta_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1UpdateMetaSchemaResponse**](../../models/V1beta1UpdateMetaSchemaResponse.md) |  | 


#### shield_service_update_meta_schema.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_meta_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_meta_schema.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_meta_schema.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_meta_schema.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_meta_schema.ApiResponseForDefault
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

