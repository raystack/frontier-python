#!/usr/bin/env python3
"""
Example demonstrating how to list users using python client
"""

from pprint import pprint
from frontier_api import *
from frontier_api.api import user_api
from frontier_api.models.v1beta1_list_users_response import V1beta1ListUsersResponse

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
        api_instance = user_api.UserApi(api_client)
        try:
            api_response = api_instance.frontier_service_list_users()
            assert isinstance(api_response, V1beta1ListUsersResponse)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling user_api->FrontierServiceListUsers: %s\n" % e)


if __name__ == "__main__":
    fetch_users()