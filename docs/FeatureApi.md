# frontier_api.FeatureApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_feature**](FeatureApi.md#frontier_service_create_feature) | **POST** /v1beta1/billing/features | Create feature
[**frontier_service_get_feature**](FeatureApi.md#frontier_service_get_feature) | **GET** /v1beta1/billing/features/{id} | Get feature
[**frontier_service_list_features**](FeatureApi.md#frontier_service_list_features) | **GET** /v1beta1/billing/features | List features
[**frontier_service_update_feature**](FeatureApi.md#frontier_service_update_feature) | **PUT** /v1beta1/billing/features/{id} | Update feature


# **frontier_service_create_feature**
> V1beta1CreateFeatureResponse frontier_service_create_feature(body)

Create feature

Create a new feature for platform.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_feature_request import V1beta1CreateFeatureRequest
from frontier_api.models.v1beta1_create_feature_response import V1beta1CreateFeatureResponse
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
    api_instance = frontier_api.FeatureApi(api_client)
    body = frontier_api.V1beta1CreateFeatureRequest() # V1beta1CreateFeatureRequest | 

    try:
        # Create feature
        api_response = api_instance.frontier_service_create_feature(body)
        print("The response of FeatureApi->frontier_service_create_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->frontier_service_create_feature: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CreateFeatureRequest**](V1beta1CreateFeatureRequest.md)|  | 

### Return type

[**V1beta1CreateFeatureResponse**](V1beta1CreateFeatureResponse.md)

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

# **frontier_service_get_feature**
> V1beta1GetFeatureResponse frontier_service_get_feature(id)

Get feature

Get a feature by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_feature_response import V1beta1GetFeatureResponse
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
    api_instance = frontier_api.FeatureApi(api_client)
    id = 'id_example' # str | ID of the feature to get

    try:
        # Get feature
        api_response = api_instance.frontier_service_get_feature(id)
        print("The response of FeatureApi->frontier_service_get_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->frontier_service_get_feature: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the feature to get | 

### Return type

[**V1beta1GetFeatureResponse**](V1beta1GetFeatureResponse.md)

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

# **frontier_service_list_features**
> V1beta1ListFeaturesResponse frontier_service_list_features()

List features

List all features of a platform.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_features_response import V1beta1ListFeaturesResponse
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
    api_instance = frontier_api.FeatureApi(api_client)

    try:
        # List features
        api_response = api_instance.frontier_service_list_features()
        print("The response of FeatureApi->frontier_service_list_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->frontier_service_list_features: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListFeaturesResponse**](V1beta1ListFeaturesResponse.md)

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

# **frontier_service_update_feature**
> V1beta1UpdateFeatureResponse frontier_service_update_feature(id, body)

Update feature

Update a feature by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_update_feature_request import FrontierServiceUpdateFeatureRequest
from frontier_api.models.v1beta1_update_feature_response import V1beta1UpdateFeatureResponse
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
    api_instance = frontier_api.FeatureApi(api_client)
    id = 'id_example' # str | ID of the feature to update
    body = frontier_api.FrontierServiceUpdateFeatureRequest() # FrontierServiceUpdateFeatureRequest | 

    try:
        # Update feature
        api_response = api_instance.frontier_service_update_feature(id, body)
        print("The response of FeatureApi->frontier_service_update_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->frontier_service_update_feature: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the feature to update | 
 **body** | [**FrontierServiceUpdateFeatureRequest**](FrontierServiceUpdateFeatureRequest.md)|  | 

### Return type

[**V1beta1UpdateFeatureResponse**](V1beta1UpdateFeatureResponse.md)

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

