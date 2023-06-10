#!/usr/bin/env python3

import time
from pprint import pprint
from shield_api import *
from shield_api.apis.tags import user_api
from shield_api.model.rpc_status import RpcStatus
from shield_api.model.v1beta1_list_users_response import V1beta1ListUsersResponse
from shield_api.model.v1beta1_list_auth_strategies_response import V1beta1ListAuthStrategiesResponse

HOST = "http://127.0.0.1:7400"

# Defining the host is optional and defaults to http://127.0.0.1:7400
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host = HOST
)

def fetch_users():
    # Enter a context with an instance of the API client
    with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = user_api.ShieldServiceListUsers(api_client)
        try:
            api_response = api_instance.shield_service_list_users()
            assert isinstance(api_response.body, V1beta1ListUsersResponse)
            pprint(api_response.body)
        except ApiException as e:
            print("Exception when calling user_api->ShieldServiceListUsers: %s\n" % e)
fetch_users()