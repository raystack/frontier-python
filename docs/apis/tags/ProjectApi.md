<a id="__pageTop"></a>
# shield_api.apis.tags.project_api.ProjectApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_list_projects**](#admin_service_list_projects) | **get** /v1beta1/admin/projects | List all projects
[**shield_service_create_project**](#shield_service_create_project) | **post** /v1beta1/projects | Create project
[**shield_service_delete_project**](#shield_service_delete_project) | **delete** /v1beta1/projects/{id} | Delete Project
[**shield_service_disable_project**](#shield_service_disable_project) | **post** /v1beta1/projects/{id}/disable | Disable project
[**shield_service_enable_project**](#shield_service_enable_project) | **post** /v1beta1/projects/{id}/enable | Enable project
[**shield_service_get_project**](#shield_service_get_project) | **get** /v1beta1/projects/{id} | Get project
[**shield_service_list_project_admins**](#shield_service_list_project_admins) | **get** /v1beta1/projects/{id}/admins | List project admins
[**shield_service_list_project_users**](#shield_service_list_project_users) | **get** /v1beta1/projects/{id}/users | List project users
[**shield_service_update_project**](#shield_service_update_project) | **put** /v1beta1/projects/{id} | Update project

# **admin_service_list_projects**
<a id="admin_service_list_projects"></a>
> V1beta1ListProjectsResponse admin_service_list_projects()

List all projects

Lists all the projects from all the organizations in a Shield instance. It can be filtered by organization and state.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
from shield_api.model.v1beta1_list_projects_response import V1beta1ListProjectsResponse
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only optional values
    query_params = {
        'orgId': "orgId_example",
        'state': "state_example",
    }
    try:
        # List all projects
        api_response = api_instance.admin_service_list_projects(
            query_params=query_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->admin_service_list_projects: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orgId | OrgIdSchema | | optional
state | StateSchema | | optional


# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#admin_service_list_projects.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#admin_service_list_projects.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#admin_service_list_projects.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#admin_service_list_projects.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#admin_service_list_projects.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#admin_service_list_projects.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#admin_service_list_projects.ApiResponseForDefault) | An unexpected error response.

#### admin_service_list_projects.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1ListProjectsResponse**](../../models/V1beta1ListProjectsResponse.md) |  | 


#### admin_service_list_projects.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_list_projects.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_list_projects.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_list_projects.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_list_projects.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### admin_service_list_projects.ApiResponseForDefault
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

# **shield_service_create_project**
<a id="shield_service_create_project"></a>
> V1beta1CreateProjectResponse shield_service_create_project(body)

Create project

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
from shield_api.model.v1beta1_project_request_body import V1beta1ProjectRequestBody
from shield_api.model.v1beta1_create_project_response import V1beta1CreateProjectResponse
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    body = V1beta1ProjectRequestBody(
        name="name_example",
        title="title_example",
        metadata=dict(),
        org_id="org_id_example",
    )
    try:
        # Create project
        api_response = api_instance.shield_service_create_project(
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_create_project: %s\n" % e)
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
[**V1beta1ProjectRequestBody**](../../models/V1beta1ProjectRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shield_service_create_project.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_create_project.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_create_project.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_create_project.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_create_project.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_create_project.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_create_project.ApiResponseForDefault) | An unexpected error response.

#### shield_service_create_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CreateProjectResponse**](../../models/V1beta1CreateProjectResponse.md) |  | 


#### shield_service_create_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_create_project.ApiResponseForDefault
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

# **shield_service_delete_project**
<a id="shield_service_delete_project"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} shield_service_delete_project(id)

Delete Project

Delete a project all of its relations permanently.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete Project
        api_response = api_instance.shield_service_delete_project(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_delete_project: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_delete_project.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_delete_project.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_delete_project.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_delete_project.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_delete_project.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_delete_project.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_delete_project.ApiResponseForDefault) | An unexpected error response.

#### shield_service_delete_project.ApiResponseFor200
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

#### shield_service_delete_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_delete_project.ApiResponseForDefault
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

# **shield_service_disable_project**
<a id="shield_service_disable_project"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} shield_service_disable_project(idbody)

Disable project

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = dict()
    try:
        # Disable project
        api_response = api_instance.shield_service_disable_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_disable_project: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_disable_project.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_disable_project.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_disable_project.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_disable_project.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_disable_project.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_disable_project.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_disable_project.ApiResponseForDefault) | An unexpected error response.

#### shield_service_disable_project.ApiResponseFor200
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

#### shield_service_disable_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_disable_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_disable_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_disable_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_disable_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_disable_project.ApiResponseForDefault
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

# **shield_service_enable_project**
<a id="shield_service_enable_project"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} shield_service_enable_project(idbody)

Enable project

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = dict()
    try:
        # Enable project
        api_response = api_instance.shield_service_enable_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_enable_project: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_enable_project.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_enable_project.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_enable_project.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_enable_project.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_enable_project.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_enable_project.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_enable_project.ApiResponseForDefault) | An unexpected error response.

#### shield_service_enable_project.ApiResponseFor200
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

#### shield_service_enable_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_enable_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_enable_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_enable_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_enable_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_enable_project.ApiResponseForDefault
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

# **shield_service_get_project**
<a id="shield_service_get_project"></a>
> V1beta1GetProjectResponse shield_service_get_project(id)

Get project

Returns a project by ID

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
from shield_api.model.v1beta1_get_project_response import V1beta1GetProjectResponse
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get project
        api_response = api_instance.shield_service_get_project(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_get_project: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_get_project.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_get_project.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_get_project.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_get_project.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_get_project.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_get_project.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_get_project.ApiResponseForDefault) | An unexpected error response.

#### shield_service_get_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1GetProjectResponse**](../../models/V1beta1GetProjectResponse.md) |  | 


#### shield_service_get_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_get_project.ApiResponseForDefault
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

# **shield_service_list_project_admins**
<a id="shield_service_list_project_admins"></a>
> V1beta1ListProjectAdminsResponse shield_service_list_project_admins(id)

List project admins

Returns a collection of admins of a project

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
from shield_api.model.v1beta1_list_project_admins_response import V1beta1ListProjectAdminsResponse
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # List project admins
        api_response = api_instance.shield_service_list_project_admins(
            path_params=path_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_list_project_admins: %s\n" % e)
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
200 | [ApiResponseFor200](#shield_service_list_project_admins.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_list_project_admins.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_list_project_admins.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_list_project_admins.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_list_project_admins.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_list_project_admins.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_list_project_admins.ApiResponseForDefault) | An unexpected error response.

#### shield_service_list_project_admins.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1ListProjectAdminsResponse**](../../models/V1beta1ListProjectAdminsResponse.md) |  | 


#### shield_service_list_project_admins.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_admins.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_admins.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_admins.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_admins.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_admins.ApiResponseForDefault
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

# **shield_service_list_project_users**
<a id="shield_service_list_project_users"></a>
> V1beta1ListProjectUsersResponse shield_service_list_project_users(id)

List project users

Returns a collection of users of a project. Filter by user permissions is supported.

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
from shield_api.model.v1beta1_list_project_users_response import V1beta1ListProjectUsersResponse
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    try:
        # List project users
        api_response = api_instance.shield_service_list_project_users(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_list_project_users: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'permissionFilter': "permissionFilter_example",
    }
    try:
        # List project users
        api_response = api_instance.shield_service_list_project_users(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_list_project_users: %s\n" % e)
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
permissionFilter | PermissionFilterSchema | | optional


# PermissionFilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#shield_service_list_project_users.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_list_project_users.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_list_project_users.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_list_project_users.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_list_project_users.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_list_project_users.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_list_project_users.ApiResponseForDefault) | An unexpected error response.

#### shield_service_list_project_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1ListProjectUsersResponse**](../../models/V1beta1ListProjectUsersResponse.md) |  | 


#### shield_service_list_project_users.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_users.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_users.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_users.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_users.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_list_project_users.ApiResponseForDefault
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

# **shield_service_update_project**
<a id="shield_service_update_project"></a>
> V1beta1UpdateProjectResponse shield_service_update_project(idbody)

Update project

Updates a project by ID

### Example

* Basic Authentication (Basic):
```python
import shield_api
from shield_api.apis.tags import project_api
from shield_api.model.v1beta1_update_project_response import V1beta1UpdateProjectResponse
from shield_api.model.v1beta1_project_request_body import V1beta1ProjectRequestBody
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
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = V1beta1ProjectRequestBody(
        name="name_example",
        title="title_example",
        metadata=dict(),
        org_id="org_id_example",
    )
    try:
        # Update project
        api_response = api_instance.shield_service_update_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling ProjectApi->shield_service_update_project: %s\n" % e)
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
[**V1beta1ProjectRequestBody**](../../models/V1beta1ProjectRequestBody.md) |  | 


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
200 | [ApiResponseFor200](#shield_service_update_project.ApiResponseFor200) | A successful response.
400 | [ApiResponseFor400](#shield_service_update_project.ApiResponseFor400) | Bad Request - The request was malformed or contained invalid parameters.
401 | [ApiResponseFor401](#shield_service_update_project.ApiResponseFor401) | Unauthorized - Authentication is required
403 | [ApiResponseFor403](#shield_service_update_project.ApiResponseFor403) | Forbidden - User does not have permission to access the resource
404 | [ApiResponseFor404](#shield_service_update_project.ApiResponseFor404) | Not Found - The requested resource was not found
500 | [ApiResponseFor500](#shield_service_update_project.ApiResponseFor500) | Internal Server Error. Returned when theres is something wrong with Shield server.
default | [ApiResponseForDefault](#shield_service_update_project.ApiResponseForDefault) | An unexpected error response.

#### shield_service_update_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1UpdateProjectResponse**](../../models/V1beta1UpdateProjectResponse.md) |  | 


#### shield_service_update_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RpcStatus**](../../models/RpcStatus.md) |  | 


#### shield_service_update_project.ApiResponseForDefault
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

