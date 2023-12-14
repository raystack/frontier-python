# frontier_api.PlanApi

All URIs are relative to *http://127.0.0.1:7400*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontier_service_create_plan**](PlanApi.md#frontier_service_create_plan) | **POST** /v1beta1/billing/plans | Create plan
[**frontier_service_get_plan**](PlanApi.md#frontier_service_get_plan) | **GET** /v1beta1/billing/plans/{id} | Get plan
[**frontier_service_list_plans**](PlanApi.md#frontier_service_list_plans) | **GET** /v1beta1/billing/plans | List plans
[**frontier_service_update_plan**](PlanApi.md#frontier_service_update_plan) | **PUT** /v1beta1/billing/plans/{id} | Update plan


# **frontier_service_create_plan**
> V1beta1CreatePlanResponse frontier_service_create_plan(body)

Create plan

Create a new plan for platform.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_create_plan_request import V1beta1CreatePlanRequest
from frontier_api.models.v1beta1_create_plan_response import V1beta1CreatePlanResponse
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
    api_instance = frontier_api.PlanApi(api_client)
    body = frontier_api.V1beta1CreatePlanRequest() # V1beta1CreatePlanRequest | 

    try:
        # Create plan
        api_response = api_instance.frontier_service_create_plan(body)
        print("The response of PlanApi->frontier_service_create_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->frontier_service_create_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CreatePlanRequest**](V1beta1CreatePlanRequest.md)|  | 

### Return type

[**V1beta1CreatePlanResponse**](V1beta1CreatePlanResponse.md)

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

# **frontier_service_get_plan**
> V1beta1GetPlanResponse frontier_service_get_plan(id)

Get plan

Get a plan by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_get_plan_response import V1beta1GetPlanResponse
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
    api_instance = frontier_api.PlanApi(api_client)
    id = 'id_example' # str | ID of the plan to get

    try:
        # Get plan
        api_response = api_instance.frontier_service_get_plan(id)
        print("The response of PlanApi->frontier_service_get_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->frontier_service_get_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the plan to get | 

### Return type

[**V1beta1GetPlanResponse**](V1beta1GetPlanResponse.md)

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

# **frontier_service_list_plans**
> V1beta1ListPlansResponse frontier_service_list_plans()

List plans

List all plans.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.v1beta1_list_plans_response import V1beta1ListPlansResponse
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
    api_instance = frontier_api.PlanApi(api_client)

    try:
        # List plans
        api_response = api_instance.frontier_service_list_plans()
        print("The response of PlanApi->frontier_service_list_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->frontier_service_list_plans: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**V1beta1ListPlansResponse**](V1beta1ListPlansResponse.md)

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

# **frontier_service_update_plan**
> V1beta1UpdatePlanResponse frontier_service_update_plan(id, body)

Update plan

Update a plan by ID.

### Example

* Basic Authentication (Basic):
```python
import time
import os
import frontier_api
from frontier_api.models.frontier_service_update_plan_request import FrontierServiceUpdatePlanRequest
from frontier_api.models.v1beta1_update_plan_response import V1beta1UpdatePlanResponse
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
    api_instance = frontier_api.PlanApi(api_client)
    id = 'id_example' # str | ID of the plan to update
    body = frontier_api.FrontierServiceUpdatePlanRequest() # FrontierServiceUpdatePlanRequest | 

    try:
        # Update plan
        api_response = api_instance.frontier_service_update_plan(id, body)
        print("The response of PlanApi->frontier_service_update_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->frontier_service_update_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the plan to update | 
 **body** | [**FrontierServiceUpdatePlanRequest**](FrontierServiceUpdatePlanRequest.md)|  | 

### Return type

[**V1beta1UpdatePlanResponse**](V1beta1UpdatePlanResponse.md)

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

