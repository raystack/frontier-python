# frontier_api.MetaSchemaApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_meta_schema**](MetaSchemaApi.md#frontier_service_create_meta_schema) | **POST** /v1beta1/meta/schemas | Create metaschema
[**frontier_service_delete_meta_schema**](MetaSchemaApi.md#frontier_service_delete_meta_schema) | **DELETE** /v1beta1/meta/schemas/{id} | Delete metaschema
[**frontier_service_get_meta_schema**](MetaSchemaApi.md#frontier_service_get_meta_schema) | **GET** /v1beta1/meta/schemas/{id} | Get metaschema
[**frontier_service_list_meta_schemas**](MetaSchemaApi.md#frontier_service_list_meta_schemas) | **GET** /v1beta1/meta/schemas | List metaschemas
[**frontier_service_update_meta_schema**](MetaSchemaApi.md#frontier_service_update_meta_schema) | **PUT** /v1beta1/meta/schemas/{id} | Update metaschema


# **frontier_service_create_meta_schema**
> V1beta1CreateMetaSchemaResponse frontier_service_create_meta_schema(body)

Create metaschema

Create a new metadata schema. The metaschema **name** must be unique within the entire Frontier instance and can contain only alphanumeric characters, dashes and underscores. The metaschema **schema** must be a valid JSON schema.Please refer to https://json-schema.org/ to know more about json schema. <br/>*Example:* `{name:\"user\",schema:{\"type\":\"object\",\"properties\":{\"label\":{\"type\":\"object\",\"additionalProperties\":{\"type\":\"string\"}},\"description\":{\"type\":\"string\"}}}}`

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_meta_schema_response import V1beta1CreateMetaSchemaResponse
from frontier_api.models.v1beta1_meta_schema_request_body import V1beta1MetaSchemaRequestBody
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
    api_instance = frontier_api.MetaSchemaApi(api_client)
    body = frontier_api.V1beta1MetaSchemaRequestBody() # V1beta1MetaSchemaRequestBody | 

    try:
        # Create metaschema
        api_response = api_instance.frontier_service_create_meta_schema(body)
        print("The response of MetaSchemaApi->frontier_service_create_meta_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaSchemaApi->frontier_service_create_meta_schema: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1MetaSchemaRequestBody**](V1beta1MetaSchemaRequestBody.md)|  | 

### Return type

[**V1beta1CreateMetaSchemaResponse**](V1beta1CreateMetaSchemaResponse.md)

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

# **frontier_service_delete_meta_schema**
> object frontier_service_delete_meta_schema(id)

Delete metaschema

Delete a metadata schema permanently. Once deleted the metaschema won't be used to validate the metadata. For example, if a metaschema(with `label` and `description` fields) is used to validate the metadata of a user, then deleting the metaschema will not validate the metadata of the user and metadata field can contain any key-value pair(and say another field called `foo` can be inserted in a user's metadata).

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
    api_instance = frontier_api.MetaSchemaApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete metaschema
        api_response = api_instance.frontier_service_delete_meta_schema(id)
        print("The response of MetaSchemaApi->frontier_service_delete_meta_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaSchemaApi->frontier_service_delete_meta_schema: %s\n" % e)
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

# **frontier_service_get_meta_schema**
> V1beta1GetMetaSchemaResponse frontier_service_get_meta_schema(id)

Get metaschema

Get a metadata schema by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_meta_schema_response import V1beta1GetMetaSchemaResponse
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
    api_instance = frontier_api.MetaSchemaApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get metaschema
        api_response = api_instance.frontier_service_get_meta_schema(id)
        print("The response of MetaSchemaApi->frontier_service_get_meta_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaSchemaApi->frontier_service_get_meta_schema: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1beta1GetMetaSchemaResponse**](V1beta1GetMetaSchemaResponse.md)

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

# **frontier_service_list_meta_schemas**
> V1beta1ListMetaSchemasResponse frontier_service_list_meta_schemas()

List metaschemas

Returns a list of all metaschemas configured on an instance level in Frontier. e.g user, project, organization etc

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_meta_schemas_response import V1beta1ListMetaSchemasResponse
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
    api_instance = frontier_api.MetaSchemaApi(api_client)

    try:
        # List metaschemas
        api_response = api_instance.frontier_service_list_meta_schemas()
        print("The response of MetaSchemaApi->frontier_service_list_meta_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaSchemaApi->frontier_service_list_meta_schemas: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListMetaSchemasResponse**](V1beta1ListMetaSchemasResponse.md)

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

# **frontier_service_update_meta_schema**
> V1beta1UpdateMetaSchemaResponse frontier_service_update_meta_schema(id, body)

Update metaschema

Update a metadata schema. Only `schema` field of a metaschema can be updated. The metaschema `schema` must be a valid JSON schema.Please refer to https://json-schema.org/ to know more about json schema. <br/>*Example:* `{name:\"user\",schema:{\"type\":\"object\",\"properties\":{\"label\":{\"type\":\"object\",\"additionalProperties\":{\"type\":\"string\"}},\"description\":{\"type\":\"string\"}}}}`

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_meta_schema_request_body import V1beta1MetaSchemaRequestBody
from frontier_api.models.v1beta1_update_meta_schema_response import V1beta1UpdateMetaSchemaResponse
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
    api_instance = frontier_api.MetaSchemaApi(api_client)
    id = 'id_example' # str | 
    body = frontier_api.V1beta1MetaSchemaRequestBody() # V1beta1MetaSchemaRequestBody | 

    try:
        # Update metaschema
        api_response = api_instance.frontier_service_update_meta_schema(id, body)
        print("The response of MetaSchemaApi->frontier_service_update_meta_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaSchemaApi->frontier_service_update_meta_schema: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**V1beta1MetaSchemaRequestBody**](V1beta1MetaSchemaRequestBody.md)|  | 

### Return type

[**V1beta1UpdateMetaSchemaResponse**](V1beta1UpdateMetaSchemaResponse.md)

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

