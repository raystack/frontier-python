# frontier_api.AuthnApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_auth_callback**](AuthnApi.md#frontier_service_auth_callback) | **GET** /v1beta1/auth/callback | Callback from a strategy
[**frontier_service_auth_callback2**](AuthnApi.md#frontier_service_auth_callback2) | **POST** /v1beta1/auth/callback | Callback from a strategy
[**frontier_service_auth_logout**](AuthnApi.md#frontier_service_auth_logout) | **GET** /v1beta1/auth/logout | Logout from a strategy
[**frontier_service_auth_logout2**](AuthnApi.md#frontier_service_auth_logout2) | **DELETE** /v1beta1/auth/logout | Logout from a strategy
[**frontier_service_auth_token**](AuthnApi.md#frontier_service_auth_token) | **POST** /v1beta1/auth/token | Generate access token by given credentials
[**frontier_service_authenticate**](AuthnApi.md#frontier_service_authenticate) | **GET** /v1beta1/auth/register/{strategyName} | Authenticate with a strategy
[**frontier_service_authenticate2**](AuthnApi.md#frontier_service_authenticate2) | **POST** /v1beta1/auth/register/{strategyName} | Authenticate with a strategy
[**frontier_service_list_auth_strategies**](AuthnApi.md#frontier_service_list_auth_strategies) | **GET** /v1beta1/auth | List authentication strategies


# **frontier_service_auth_callback**
> object frontier_service_auth_callback(strategy_name=strategy_name, state=state, code=code, state_options=state_options)

Callback from a strategy

Callback from a strategy. This is the endpoint where the strategy will redirect the user after successful authentication. This endpoint will be called with the code and state query parameters. The code will be used to get the access token from the strategy and the state will be used to get the return_to url from the session and redirect the user to that url.

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
    api_instance = frontier_api.AuthnApi(api_client)
    strategy_name = 'strategy_name_example' # str | strategy_name will not be set for oidc but can be utilized for methods like email magic links (optional)
    state = 'state_example' # str | for oidc & magic links (optional)
    code = 'code_example' # str |  (optional)
    state_options = None # object | state_options has additional configurations for the authentication flow at hand for example, in case of passkey, it has challenge and public key (optional)

    try:
        # Callback from a strategy
        api_response = api_instance.frontier_service_auth_callback(strategy_name=strategy_name, state=state, code=code, state_options=state_options)
        print("The response of AuthnApi->frontier_service_auth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_auth_callback: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_name** | **str**| strategy_name will not be set for oidc but can be utilized for methods like email magic links | [optional] 
 **state** | **str**| for oidc &amp; magic links | [optional] 
 **code** | **str**|  | [optional] 
 **state_options** | [**object**](.md)| state_options has additional configurations for the authentication flow at hand for example, in case of passkey, it has challenge and public key | [optional] 

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

# **frontier_service_auth_callback2**
> object frontier_service_auth_callback2(body)

Callback from a strategy

Callback from a strategy. This is the endpoint where the strategy will redirect the user after successful authentication. This endpoint will be called with the code and state query parameters. The code will be used to get the access token from the strategy and the state will be used to get the return_to url from the session and redirect the user to that url.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_auth_callback_request import V1beta1AuthCallbackRequest
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
    api_instance = frontier_api.AuthnApi(api_client)
    body = frontier_api.V1beta1AuthCallbackRequest() # V1beta1AuthCallbackRequest | 

    try:
        # Callback from a strategy
        api_response = api_instance.frontier_service_auth_callback2(body)
        print("The response of AuthnApi->frontier_service_auth_callback2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_auth_callback2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1AuthCallbackRequest**](V1beta1AuthCallbackRequest.md)|  | 

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

# **frontier_service_auth_logout**
> object frontier_service_auth_logout()

Logout from a strategy

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
    api_instance = frontier_api.AuthnApi(api_client)

    try:
        # Logout from a strategy
        api_response = api_instance.frontier_service_auth_logout()
        print("The response of AuthnApi->frontier_service_auth_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_auth_logout: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **frontier_service_auth_logout2**
> object frontier_service_auth_logout2()

Logout from a strategy

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
    api_instance = frontier_api.AuthnApi(api_client)

    try:
        # Logout from a strategy
        api_response = api_instance.frontier_service_auth_logout2()
        print("The response of AuthnApi->frontier_service_auth_logout2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_auth_logout2: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **frontier_service_auth_token**
> V1beta1AuthTokenResponse frontier_service_auth_token(body)

Generate access token by given credentials

Access token can be generated by providing the credentials in the request body/header. The credentials can be client id and secret or service account generated key jwt. Use the generated access token in Authorization header to access the frontier resources.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_auth_token_request import V1beta1AuthTokenRequest
from frontier_api.models.v1beta1_auth_token_response import V1beta1AuthTokenResponse
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
    api_instance = frontier_api.AuthnApi(api_client)
    body = frontier_api.V1beta1AuthTokenRequest() # V1beta1AuthTokenRequest | 

    try:
        # Generate access token by given credentials
        api_response = api_instance.frontier_service_auth_token(body)
        print("The response of AuthnApi->frontier_service_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_auth_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1AuthTokenRequest**](V1beta1AuthTokenRequest.md)|  | 

### Return type

[**V1beta1AuthTokenResponse**](V1beta1AuthTokenResponse.md)

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

# **frontier_service_authenticate**
> V1beta1AuthenticateResponse frontier_service_authenticate(strategy_name, redirect_onstart=redirect_onstart, return_to=return_to, email=email, callback_url=callback_url)

Authenticate with a strategy

Authenticate a user with a strategy. By default, after successful authentication no operation will be performed to apply redirection in case of browsers, provide a url in the authenticate request body that will be used for redirection after authentication. Also set redirect as true for redirecting the user request to the redirect_url after successful authentication.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_authenticate_response import V1beta1AuthenticateResponse
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
    api_instance = frontier_api.AuthnApi(api_client)
    strategy_name = 'strategy_name_example' # str | Name of the strategy to use for authentication.<br/> *Example:* `google`
    redirect_onstart = True # bool | by default, location redirect header for starting authentication flow if applicable will be skipped unless this is set to true, useful in browser, same value will also be returned as endpoint in response anyway  If set to true, location header will be set for redirect to start auth flow (optional)
    return_to = 'return_to_example' # str | by default, after successful authentication(flow completes) no operation will be performed, to apply redirection in case of browsers, provide an url that will be used after authentication where users are sent from frontier. return_to should be one of the allowed urls configured at instance level  URL to redirect after successful authentication.<br/> *Example:*`\"https://frontier.example.com\"` (optional)
    email = 'email_example' # str | email of the user for magic links  Email of the user to authenticate. Used for magic links.<br/> *Example:*`example@acme.org` (optional)
    callback_url = 'callback_url_example' # str | callback_url will be used by strategy as last step to finish authentication flow in OIDC this host will receive \"state\" and \"code\" query params, in case of magic links this will be the url where user is redirected after clicking on magic link. For most cases it could be host of frontier but in case of proxies, this will be proxy public endpoint. callback_url should be one of the allowed urls configured at instance level  Host which should handle the call to finish authentication flow, for most cases it could be host of frontier but in case of proxies, this will be proxy public endpoint.<br/> *Example:*`https://frontier.example.com/v1beta1/auth/callback` (optional)

    try:
        # Authenticate with a strategy
        api_response = api_instance.frontier_service_authenticate(strategy_name, redirect_onstart=redirect_onstart, return_to=return_to, email=email, callback_url=callback_url)
        print("The response of AuthnApi->frontier_service_authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_authenticate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_name** | **str**| Name of the strategy to use for authentication.&lt;br/&gt; *Example:* &#x60;google&#x60; | 
 **redirect_onstart** | **bool**| by default, location redirect header for starting authentication flow if applicable will be skipped unless this is set to true, useful in browser, same value will also be returned as endpoint in response anyway  If set to true, location header will be set for redirect to start auth flow | [optional] 
 **return_to** | **str**| by default, after successful authentication(flow completes) no operation will be performed, to apply redirection in case of browsers, provide an url that will be used after authentication where users are sent from frontier. return_to should be one of the allowed urls configured at instance level  URL to redirect after successful authentication.&lt;br/&gt; *Example:*&#x60;\&quot;https://frontier.example.com\&quot;&#x60; | [optional] 
 **email** | **str**| email of the user for magic links  Email of the user to authenticate. Used for magic links.&lt;br/&gt; *Example:*&#x60;example@acme.org&#x60; | [optional] 
 **callback_url** | **str**| callback_url will be used by strategy as last step to finish authentication flow in OIDC this host will receive \&quot;state\&quot; and \&quot;code\&quot; query params, in case of magic links this will be the url where user is redirected after clicking on magic link. For most cases it could be host of frontier but in case of proxies, this will be proxy public endpoint. callback_url should be one of the allowed urls configured at instance level  Host which should handle the call to finish authentication flow, for most cases it could be host of frontier but in case of proxies, this will be proxy public endpoint.&lt;br/&gt; *Example:*&#x60;https://frontier.example.com/v1beta1/auth/callback&#x60; | [optional] 

### Return type

[**V1beta1AuthenticateResponse**](V1beta1AuthenticateResponse.md)

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

# **frontier_service_authenticate2**
> V1beta1AuthenticateResponse frontier_service_authenticate2(strategy_name, body)

Authenticate with a strategy

Authenticate a user with a strategy. By default, after successful authentication no operation will be performed to apply redirection in case of browsers, provide a url in the authenticate request body that will be used for redirection after authentication. Also set redirect as true for redirecting the user request to the redirect_url after successful authentication.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_authenticate2_request import FrontierServiceAuthenticate2Request
from frontier_api.models.v1beta1_authenticate_response import V1beta1AuthenticateResponse
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
    api_instance = frontier_api.AuthnApi(api_client)
    strategy_name = 'strategy_name_example' # str | Name of the strategy to use for authentication.<br/> *Example:* `google`
    body = frontier_api.FrontierServiceAuthenticate2Request() # FrontierServiceAuthenticate2Request | 

    try:
        # Authenticate with a strategy
        api_response = api_instance.frontier_service_authenticate2(strategy_name, body)
        print("The response of AuthnApi->frontier_service_authenticate2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_authenticate2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_name** | **str**| Name of the strategy to use for authentication.&lt;br/&gt; *Example:* &#x60;google&#x60; | 
 **body** | [**FrontierServiceAuthenticate2Request**](FrontierServiceAuthenticate2Request.md)|  | 

### Return type

[**V1beta1AuthenticateResponse**](V1beta1AuthenticateResponse.md)

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

# **frontier_service_list_auth_strategies**
> V1beta1ListAuthStrategiesResponse frontier_service_list_auth_strategies()

List authentication strategies

Returns a list of identity providers configured on an instance level in Frontier. e.g Google, AzureAD, Github etc

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_auth_strategies_response import V1beta1ListAuthStrategiesResponse
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
    api_instance = frontier_api.AuthnApi(api_client)

    try:
        # List authentication strategies
        api_response = api_instance.frontier_service_list_auth_strategies()
        print("The response of AuthnApi->frontier_service_list_auth_strategies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthnApi->frontier_service_list_auth_strategies: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListAuthStrategiesResponse**](V1beta1ListAuthStrategiesResponse.md)

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

