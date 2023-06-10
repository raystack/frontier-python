# shield-python
The Shield APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Shield APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Shield APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Shield into your existing applications and workflows.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.2.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.raystack.org/](https://www.raystack.org/)

## Requirements.

Python &gt;&#x3D;3.7

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/raystack/shield-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/raystack/shield-python.git`)

Then import the package:
```python
import shield_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import shield_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import shield_api
from pprint import pprint
from shield_api.apis.tags import authn_api
from shield_api.model.rpc_status import RpcStatus
from shield_api.model.v1beta1_authenticate_response import V1beta1AuthenticateResponse
from shield_api.model.v1beta1_list_auth_strategies_response import V1beta1ListAuthStrategiesResponse
# Defining the host is optional and defaults to http://127.0.0.1:7400
# See configuration.py for a list of all supported configuration parameters.
configuration = shield_api.Configuration(
    host = "http://127.0.0.1:7400"
)


# Enter a context with an instance of the API client
with shield_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authn_api.AuthnApi(api_client)
    strategy_name = "strategyName_example" # str | strategy_name will not be set for oidc but can be utilized for methods like email magic links (optional)
state = "state_example" # str | for oidc & magic links (optional)
code = "code_example" # str |  (optional)

    try:
        # Callback from a strategy
        api_response = api_instance.shield_service_auth_callback(strategy_name=strategy_namestate=statecode=code)
        pprint(api_response)
    except shield_api.ApiException as e:
        print("Exception when calling AuthnApi->shield_service_auth_callback: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:7400*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthnApi* | [**shield_service_auth_callback**](docs/apis/tags/AuthnApi.md#shield_service_auth_callback) | **get** /v1beta1/auth/callback | Callback from a strategy
*AuthnApi* | [**shield_service_auth_callback2**](docs/apis/tags/AuthnApi.md#shield_service_auth_callback2) | **post** /v1beta1/auth/callback | Callback from a strategy
*AuthnApi* | [**shield_service_auth_logout**](docs/apis/tags/AuthnApi.md#shield_service_auth_logout) | **get** /v1beta1/auth/logout | Logout from a strategy
*AuthnApi* | [**shield_service_auth_logout2**](docs/apis/tags/AuthnApi.md#shield_service_auth_logout2) | **delete** /v1beta1/auth/logout | Logout from a strategy
*AuthnApi* | [**shield_service_authenticate**](docs/apis/tags/AuthnApi.md#shield_service_authenticate) | **get** /v1beta1/auth/register/{strategyName} | Authenticate with a strategy
*AuthnApi* | [**shield_service_authenticate2**](docs/apis/tags/AuthnApi.md#shield_service_authenticate2) | **post** /v1beta1/auth/register/{strategyName} | Authenticate with a strategy
*AuthnApi* | [**shield_service_list_auth_strategies**](docs/apis/tags/AuthnApi.md#shield_service_list_auth_strategies) | **get** /v1beta1/auth | List authentication strategies
*AuthzApi* | [**shield_service_check_resource_permission**](docs/apis/tags/AuthzApi.md#shield_service_check_resource_permission) | **post** /v1beta1/check | Check
*AuthzApi* | [**shield_service_get_jwks**](docs/apis/tags/AuthzApi.md#shield_service_get_jwks) | **get** /v1beta1/auth/jwks | Get well known JWKs
*AuthzApi* | [**shield_service_get_jwks2**](docs/apis/tags/AuthzApi.md#shield_service_get_jwks2) | **get** /.well-known/jwks.json | Get well known JWKs
*GroupApi* | [**admin_service_list_groups**](docs/apis/tags/GroupApi.md#admin_service_list_groups) | **get** /v1beta1/admin/groups | Get all groups
*GroupApi* | [**shield_service_add_group_users**](docs/apis/tags/GroupApi.md#shield_service_add_group_users) | **post** /v1beta1/organizations/{orgId}/groups/{id}/users | Add group user
*GroupApi* | [**shield_service_create_group**](docs/apis/tags/GroupApi.md#shield_service_create_group) | **post** /v1beta1/organizations/{orgId}/groups | Create Group
*GroupApi* | [**shield_service_delete_group**](docs/apis/tags/GroupApi.md#shield_service_delete_group) | **delete** /v1beta1/organizations/{orgId}/groups/{id} | Delete group
*GroupApi* | [**shield_service_disable_group**](docs/apis/tags/GroupApi.md#shield_service_disable_group) | **post** /v1beta1/organizations/{orgId}/groups/{id}/disable | Disable group
*GroupApi* | [**shield_service_enable_group**](docs/apis/tags/GroupApi.md#shield_service_enable_group) | **post** /v1beta1/organizations/{orgId}/groups/{id}/enable | Enable group
*GroupApi* | [**shield_service_get_group**](docs/apis/tags/GroupApi.md#shield_service_get_group) | **get** /v1beta1/organizations/{orgId}/groups/{id} | Get group by ID
*GroupApi* | [**shield_service_list_group_users**](docs/apis/tags/GroupApi.md#shield_service_list_group_users) | **get** /v1beta1/organizations/{orgId}/groups/{id}/users | List group users
*GroupApi* | [**shield_service_list_organization_groups**](docs/apis/tags/GroupApi.md#shield_service_list_organization_groups) | **get** /v1beta1/organizations/{orgId}/groups | List Organization Groups
*GroupApi* | [**shield_service_remove_group_user**](docs/apis/tags/GroupApi.md#shield_service_remove_group_user) | **delete** /v1beta1/organizations/{orgId}/groups/{id}/users/{userId} | Remove group user
*GroupApi* | [**shield_service_update_group**](docs/apis/tags/GroupApi.md#shield_service_update_group) | **put** /v1beta1/organizations/{orgId}/groups/{id} | Update group by ID
*MetaSchemaApi* | [**shield_service_create_meta_schema**](docs/apis/tags/MetaSchemaApi.md#shield_service_create_meta_schema) | **post** /v1beta1/meta/schemas | Create metaschema
*MetaSchemaApi* | [**shield_service_delete_meta_schema**](docs/apis/tags/MetaSchemaApi.md#shield_service_delete_meta_schema) | **delete** /v1beta1/meta/schemas/{id} | Delete metaSchema
*MetaSchemaApi* | [**shield_service_get_meta_schema**](docs/apis/tags/MetaSchemaApi.md#shield_service_get_meta_schema) | **get** /v1beta1/meta/schemas/{id} | Get metaSchema
*MetaSchemaApi* | [**shield_service_list_meta_schemas**](docs/apis/tags/MetaSchemaApi.md#shield_service_list_meta_schemas) | **get** /v1beta1/meta/schemas | List metaschemas
*MetaSchemaApi* | [**shield_service_update_meta_schema**](docs/apis/tags/MetaSchemaApi.md#shield_service_update_meta_schema) | **put** /v1beta1/meta/schemas/{id} | Update metaSchema
*NamespaceApi* | [**shield_service_get_namespace**](docs/apis/tags/NamespaceApi.md#shield_service_get_namespace) | **get** /v1beta1/namespaces/{id} | Get a Namespaces
*NamespaceApi* | [**shield_service_list_namespaces**](docs/apis/tags/NamespaceApi.md#shield_service_list_namespaces) | **get** /v1beta1/namespaces | Get all Namespaces
*OrganizationApi* | [**admin_service_list_all_organizations**](docs/apis/tags/OrganizationApi.md#admin_service_list_all_organizations) | **get** /v1beta1/admin/organizations | Get all organization
*OrganizationApi* | [**shield_service_accept_organization_invitation**](docs/apis/tags/OrganizationApi.md#shield_service_accept_organization_invitation) | **post** /v1beta1/organizations/{orgId}/invitations/{id}/accept | Accept pending invitation
*OrganizationApi* | [**shield_service_add_organization_users**](docs/apis/tags/OrganizationApi.md#shield_service_add_organization_users) | **post** /v1beta1/organizations/{id}/users | Add organization user
*OrganizationApi* | [**shield_service_create_organization**](docs/apis/tags/OrganizationApi.md#shield_service_create_organization) | **post** /v1beta1/organizations | Create organization
*OrganizationApi* | [**shield_service_create_organization_invitation**](docs/apis/tags/OrganizationApi.md#shield_service_create_organization_invitation) | **post** /v1beta1/organizations/{orgId}/invitations | Invite user
*OrganizationApi* | [**shield_service_delete_organization**](docs/apis/tags/OrganizationApi.md#shield_service_delete_organization) | **delete** /v1beta1/organizations/{id} | Delete organization
*OrganizationApi* | [**shield_service_delete_organization_invitation**](docs/apis/tags/OrganizationApi.md#shield_service_delete_organization_invitation) | **delete** /v1beta1/organizations/{orgId}/invitations/{id} | Delete pending invitation
*OrganizationApi* | [**shield_service_disable_organization**](docs/apis/tags/OrganizationApi.md#shield_service_disable_organization) | **post** /v1beta1/organizations/{id}/disable | Disable organization
*OrganizationApi* | [**shield_service_enable_organization**](docs/apis/tags/OrganizationApi.md#shield_service_enable_organization) | **post** /v1beta1/organizations/{id}/enable | Enable organization
*OrganizationApi* | [**shield_service_get_organization**](docs/apis/tags/OrganizationApi.md#shield_service_get_organization) | **get** /v1beta1/organizations/{id} | Get organization
*OrganizationApi* | [**shield_service_get_organization_invitation**](docs/apis/tags/OrganizationApi.md#shield_service_get_organization_invitation) | **get** /v1beta1/organizations/{orgId}/invitations/{id} | Get pending invitation
*OrganizationApi* | [**shield_service_list_organization_admins**](docs/apis/tags/OrganizationApi.md#shield_service_list_organization_admins) | **get** /v1beta1/organizations/{id}/admins | List organization admins
*OrganizationApi* | [**shield_service_list_organization_invitations**](docs/apis/tags/OrganizationApi.md#shield_service_list_organization_invitations) | **get** /v1beta1/organizations/{orgId}/invitations | List pending invitations
*OrganizationApi* | [**shield_service_list_organization_projects**](docs/apis/tags/OrganizationApi.md#shield_service_list_organization_projects) | **get** /v1beta1/organizations/{id}/projects | Get organization projects
*OrganizationApi* | [**shield_service_list_organization_users**](docs/apis/tags/OrganizationApi.md#shield_service_list_organization_users) | **get** /v1beta1/organizations/{id}/users | List organization users
*OrganizationApi* | [**shield_service_list_organizations**](docs/apis/tags/OrganizationApi.md#shield_service_list_organizations) | **get** /v1beta1/organizations | List organizations
*OrganizationApi* | [**shield_service_remove_organization_user**](docs/apis/tags/OrganizationApi.md#shield_service_remove_organization_user) | **delete** /v1beta1/organizations/{id}/users/{userId} | Remove organization user
*OrganizationApi* | [**shield_service_update_organization**](docs/apis/tags/OrganizationApi.md#shield_service_update_organization) | **put** /v1beta1/organizations/{id} | Update organization
*PermissionApi* | [**admin_service_create_permission**](docs/apis/tags/PermissionApi.md#admin_service_create_permission) | **post** /v1beta1/permissions | Create permission
*PermissionApi* | [**admin_service_delete_permission**](docs/apis/tags/PermissionApi.md#admin_service_delete_permission) | **delete** /v1beta1/permissions/{id} | Delete permission by ID
*PermissionApi* | [**admin_service_update_permission**](docs/apis/tags/PermissionApi.md#admin_service_update_permission) | **put** /v1beta1/permissions/{id} | Update permission by ID
*PermissionApi* | [**shield_service_get_permission**](docs/apis/tags/PermissionApi.md#shield_service_get_permission) | **get** /v1beta1/permissions/{id} | Get permission by ID
*PermissionApi* | [**shield_service_list_permissions**](docs/apis/tags/PermissionApi.md#shield_service_list_permissions) | **get** /v1beta1/permissions | Get all Permissions
*PolicyApi* | [**admin_service_list_policies**](docs/apis/tags/PolicyApi.md#admin_service_list_policies) | **get** /v1beta1/policies | Get all policies
*PolicyApi* | [**shield_service_create_policy**](docs/apis/tags/PolicyApi.md#shield_service_create_policy) | **post** /v1beta1/policies | Create policy
*PolicyApi* | [**shield_service_delete_policy**](docs/apis/tags/PolicyApi.md#shield_service_delete_policy) | **delete** /v1beta1/policies/{id} | Delete Policy
*PolicyApi* | [**shield_service_get_policy**](docs/apis/tags/PolicyApi.md#shield_service_get_policy) | **get** /v1beta1/policies/{id} | Get policy by ID
*PolicyApi* | [**shield_service_update_policy**](docs/apis/tags/PolicyApi.md#shield_service_update_policy) | **put** /v1beta1/policies/{id} | Update policy by ID
*ProjectApi* | [**admin_service_list_projects**](docs/apis/tags/ProjectApi.md#admin_service_list_projects) | **get** /v1beta1/admin/projects | Get all project
*ProjectApi* | [**shield_service_create_project**](docs/apis/tags/ProjectApi.md#shield_service_create_project) | **post** /v1beta1/projects | Create project
*ProjectApi* | [**shield_service_delete_project**](docs/apis/tags/ProjectApi.md#shield_service_delete_project) | **delete** /v1beta1/projects/{id} | Delete Project
*ProjectApi* | [**shield_service_disable_project**](docs/apis/tags/ProjectApi.md#shield_service_disable_project) | **post** /v1beta1/projects/{id}/disable | Disable project
*ProjectApi* | [**shield_service_enable_project**](docs/apis/tags/ProjectApi.md#shield_service_enable_project) | **post** /v1beta1/projects/{id}/enable | Enable project
*ProjectApi* | [**shield_service_get_project**](docs/apis/tags/ProjectApi.md#shield_service_get_project) | **get** /v1beta1/projects/{id} | Get project
*ProjectApi* | [**shield_service_list_project_admins**](docs/apis/tags/ProjectApi.md#shield_service_list_project_admins) | **get** /v1beta1/projects/{id}/admins | List project admins
*ProjectApi* | [**shield_service_list_project_users**](docs/apis/tags/ProjectApi.md#shield_service_list_project_users) | **get** /v1beta1/projects/{id}/users | List project users
*ProjectApi* | [**shield_service_update_project**](docs/apis/tags/ProjectApi.md#shield_service_update_project) | **put** /v1beta1/projects/{id} | Update project
*RelationApi* | [**admin_service_list_relations**](docs/apis/tags/RelationApi.md#admin_service_list_relations) | **get** /v1beta1/admin/relations | Get all relations
*RelationApi* | [**shield_service_create_relation**](docs/apis/tags/RelationApi.md#shield_service_create_relation) | **post** /v1beta1/relations | Create Relation
*RelationApi* | [**shield_service_delete_relation**](docs/apis/tags/RelationApi.md#shield_service_delete_relation) | **delete** /v1beta1/relations/{relation}/object/{object}/subject/{subject} | Remove a subject having a relation from an object
*RelationApi* | [**shield_service_get_relation**](docs/apis/tags/RelationApi.md#shield_service_get_relation) | **get** /v1beta1/relations/{id} | Get Relation by ID
*ResourceApi* | [**admin_service_list_resources**](docs/apis/tags/ResourceApi.md#admin_service_list_resources) | **get** /v1beta1/admin/resources | Get all resources
*ResourceApi* | [**shield_service_create_project_resource**](docs/apis/tags/ResourceApi.md#shield_service_create_project_resource) | **post** /v1beta1/projects/{projectId}/resources | Create Resource
*ResourceApi* | [**shield_service_delete_project_resource**](docs/apis/tags/ResourceApi.md#shield_service_delete_project_resource) | **delete** /v1beta1/projects/{projectId}/resources/{id} | Delete a resource permanently forever
*ResourceApi* | [**shield_service_get_project_resource**](docs/apis/tags/ResourceApi.md#shield_service_get_project_resource) | **get** /v1beta1/projects/{projectId}/resources/{id} | Get Resource by ID
*ResourceApi* | [**shield_service_list_project_resources**](docs/apis/tags/ResourceApi.md#shield_service_list_project_resources) | **get** /v1beta1/projects/{projectId}/resources | Get all resources
*ResourceApi* | [**shield_service_update_project_resource**](docs/apis/tags/ResourceApi.md#shield_service_update_project_resource) | **put** /v1beta1/projects/{projectId}/resources/{id} | Update Resource by ID
*RoleApi* | [**admin_service_create_role**](docs/apis/tags/RoleApi.md#admin_service_create_role) | **post** /v1beta1/roles | Create platform role
*RoleApi* | [**admin_service_delete_role**](docs/apis/tags/RoleApi.md#admin_service_delete_role) | **delete** /v1beta1/roles/{id} | Delete platform role
*RoleApi* | [**shield_service_create_organization_role**](docs/apis/tags/RoleApi.md#shield_service_create_organization_role) | **post** /v1beta1/organizations/{orgId}/roles | Create organization role
*RoleApi* | [**shield_service_delete_organization_role**](docs/apis/tags/RoleApi.md#shield_service_delete_organization_role) | **delete** /v1beta1/organizations/{orgId}/roles/{id} | Delete Organization Role
*RoleApi* | [**shield_service_get_organization_role**](docs/apis/tags/RoleApi.md#shield_service_get_organization_role) | **get** /v1beta1/organizations/{orgId}/roles/{id} | Get Organization Role
*RoleApi* | [**shield_service_list_organization_roles**](docs/apis/tags/RoleApi.md#shield_service_list_organization_roles) | **get** /v1beta1/organizations/{orgId}/roles | List organization roles
*RoleApi* | [**shield_service_list_roles**](docs/apis/tags/RoleApi.md#shield_service_list_roles) | **get** /v1beta1/roles | List default roles
*RoleApi* | [**shield_service_update_organization_role**](docs/apis/tags/RoleApi.md#shield_service_update_organization_role) | **put** /v1beta1/organizations/{orgId}/roles/{id} | Update organization role
*ServiceUserApi* | [**shield_service_create_service_user**](docs/apis/tags/ServiceUserApi.md#shield_service_create_service_user) | **post** /v1beta1/serviceusers | Create Service User
*ServiceUserApi* | [**shield_service_create_service_user_key**](docs/apis/tags/ServiceUserApi.md#shield_service_create_service_user_key) | **post** /v1beta1/serviceusers/{id}/keys | Create a service user key
*ServiceUserApi* | [**shield_service_create_service_user_secret**](docs/apis/tags/ServiceUserApi.md#shield_service_create_service_user_secret) | **post** /v1beta1/serviceusers/{id}/secrets | Create a service user secret
*ServiceUserApi* | [**shield_service_delete_service_user**](docs/apis/tags/ServiceUserApi.md#shield_service_delete_service_user) | **delete** /v1beta1/serviceusers/{id} | Delete a service user
*ServiceUserApi* | [**shield_service_delete_service_user_key**](docs/apis/tags/ServiceUserApi.md#shield_service_delete_service_user_key) | **delete** /v1beta1/serviceusers/{id}/keys/{keyId} | Delete a service user key
*ServiceUserApi* | [**shield_service_delete_service_user_secret**](docs/apis/tags/ServiceUserApi.md#shield_service_delete_service_user_secret) | **delete** /v1beta1/serviceusers/{id}/secrets/{secretId} | Delete a service user secret
*ServiceUserApi* | [**shield_service_get_service_user**](docs/apis/tags/ServiceUserApi.md#shield_service_get_service_user) | **get** /v1beta1/serviceusers/{id} | Get service user by id
*ServiceUserApi* | [**shield_service_get_service_user_key**](docs/apis/tags/ServiceUserApi.md#shield_service_get_service_user_key) | **get** /v1beta1/serviceusers/{id}/keys/{keyId} | Get a service user key
*ServiceUserApi* | [**shield_service_list_service_user_keys**](docs/apis/tags/ServiceUserApi.md#shield_service_list_service_user_keys) | **get** /v1beta1/serviceusers/{id}/keys | List service user keys
*ServiceUserApi* | [**shield_service_list_service_user_secrets**](docs/apis/tags/ServiceUserApi.md#shield_service_list_service_user_secrets) | **get** /v1beta1/serviceusers/{id}/secrets | List service user secrets
*ServiceUserApi* | [**shield_service_list_service_users**](docs/apis/tags/ServiceUserApi.md#shield_service_list_service_users) | **get** /v1beta1/serviceusers | List service users of an organization
*UserApi* | [**admin_service_list_all_users**](docs/apis/tags/UserApi.md#admin_service_list_all_users) | **get** /v1beta1/admin/users | Get all users
*UserApi* | [**shield_service_create_user**](docs/apis/tags/UserApi.md#shield_service_create_user) | **post** /v1beta1/users | Create user
*UserApi* | [**shield_service_delete_user**](docs/apis/tags/UserApi.md#shield_service_delete_user) | **delete** /v1beta1/users/{id} | Delete user
*UserApi* | [**shield_service_disable_user**](docs/apis/tags/UserApi.md#shield_service_disable_user) | **post** /v1beta1/users/{id}/disable | Disable user
*UserApi* | [**shield_service_enable_user**](docs/apis/tags/UserApi.md#shield_service_enable_user) | **post** /v1beta1/users/{id}/enable | Enable user
*UserApi* | [**shield_service_get_current_user**](docs/apis/tags/UserApi.md#shield_service_get_current_user) | **get** /v1beta1/users/self | Get current user
*UserApi* | [**shield_service_get_organizations_by_current_user**](docs/apis/tags/UserApi.md#shield_service_get_organizations_by_current_user) | **get** /v1beta1/users/self/organizations | Get My Organizations
*UserApi* | [**shield_service_get_organizations_by_user**](docs/apis/tags/UserApi.md#shield_service_get_organizations_by_user) | **get** /v1beta1/users/{id}/organizations | Get Organizations by User
*UserApi* | [**shield_service_get_user**](docs/apis/tags/UserApi.md#shield_service_get_user) | **get** /v1beta1/users/{id} | Get a user by id
*UserApi* | [**shield_service_list_current_user_groups**](docs/apis/tags/UserApi.md#shield_service_list_current_user_groups) | **get** /v1beta1/users/self/groups | List My Groups
*UserApi* | [**shield_service_list_user_groups**](docs/apis/tags/UserApi.md#shield_service_list_user_groups) | **get** /v1beta1/users/{id}/groups | List Groups of a User
*UserApi* | [**shield_service_list_user_invitations**](docs/apis/tags/UserApi.md#shield_service_list_user_invitations) | **get** /v1beta1/users/{id}/invitations | List User Invitations
*UserApi* | [**shield_service_list_users**](docs/apis/tags/UserApi.md#shield_service_list_users) | **get** /v1beta1/users | List public users
*UserApi* | [**shield_service_update_current_user**](docs/apis/tags/UserApi.md#shield_service_update_current_user) | **put** /v1beta1/users/self | Update current User
*UserApi* | [**shield_service_update_user**](docs/apis/tags/UserApi.md#shield_service_update_user) | **put** /v1beta1/users/{id} | Update User by ID

## Documentation For Models

 - [ProtobufAny](docs/models/ProtobufAny.md)
 - [ProtobufNullValue](docs/models/ProtobufNullValue.md)
 - [RpcStatus](docs/models/RpcStatus.md)
 - [V1beta1AuthStrategy](docs/models/V1beta1AuthStrategy.md)
 - [V1beta1AuthenticateResponse](docs/models/V1beta1AuthenticateResponse.md)
 - [V1beta1CheckResourcePermissionRequest](docs/models/V1beta1CheckResourcePermissionRequest.md)
 - [V1beta1CheckResourcePermissionResponse](docs/models/V1beta1CheckResourcePermissionResponse.md)
 - [V1beta1CreateGroupResponse](docs/models/V1beta1CreateGroupResponse.md)
 - [V1beta1CreateMetaSchemaResponse](docs/models/V1beta1CreateMetaSchemaResponse.md)
 - [V1beta1CreateOrganizationInvitationResponse](docs/models/V1beta1CreateOrganizationInvitationResponse.md)
 - [V1beta1CreateOrganizationResponse](docs/models/V1beta1CreateOrganizationResponse.md)
 - [V1beta1CreateOrganizationRoleResponse](docs/models/V1beta1CreateOrganizationRoleResponse.md)
 - [V1beta1CreatePermissionRequest](docs/models/V1beta1CreatePermissionRequest.md)
 - [V1beta1CreatePermissionResponse](docs/models/V1beta1CreatePermissionResponse.md)
 - [V1beta1CreatePolicyResponse](docs/models/V1beta1CreatePolicyResponse.md)
 - [V1beta1CreateProjectResourceResponse](docs/models/V1beta1CreateProjectResourceResponse.md)
 - [V1beta1CreateProjectResponse](docs/models/V1beta1CreateProjectResponse.md)
 - [V1beta1CreateRelationResponse](docs/models/V1beta1CreateRelationResponse.md)
 - [V1beta1CreateRoleResponse](docs/models/V1beta1CreateRoleResponse.md)
 - [V1beta1CreateServiceUserKeyResponse](docs/models/V1beta1CreateServiceUserKeyResponse.md)
 - [V1beta1CreateServiceUserRequest](docs/models/V1beta1CreateServiceUserRequest.md)
 - [V1beta1CreateServiceUserResponse](docs/models/V1beta1CreateServiceUserResponse.md)
 - [V1beta1CreateServiceUserSecretResponse](docs/models/V1beta1CreateServiceUserSecretResponse.md)
 - [V1beta1CreateUserResponse](docs/models/V1beta1CreateUserResponse.md)
 - [V1beta1GetCurrentUserResponse](docs/models/V1beta1GetCurrentUserResponse.md)
 - [V1beta1GetGroupResponse](docs/models/V1beta1GetGroupResponse.md)
 - [V1beta1GetJWKsResponse](docs/models/V1beta1GetJWKsResponse.md)
 - [V1beta1GetMetaSchemaResponse](docs/models/V1beta1GetMetaSchemaResponse.md)
 - [V1beta1GetNamespaceResponse](docs/models/V1beta1GetNamespaceResponse.md)
 - [V1beta1GetOrganizationInvitationResponse](docs/models/V1beta1GetOrganizationInvitationResponse.md)
 - [V1beta1GetOrganizationResponse](docs/models/V1beta1GetOrganizationResponse.md)
 - [V1beta1GetOrganizationRoleResponse](docs/models/V1beta1GetOrganizationRoleResponse.md)
 - [V1beta1GetOrganizationsByCurrentUserResponse](docs/models/V1beta1GetOrganizationsByCurrentUserResponse.md)
 - [V1beta1GetOrganizationsByUserResponse](docs/models/V1beta1GetOrganizationsByUserResponse.md)
 - [V1beta1GetPermissionResponse](docs/models/V1beta1GetPermissionResponse.md)
 - [V1beta1GetPolicyResponse](docs/models/V1beta1GetPolicyResponse.md)
 - [V1beta1GetProjectResourceResponse](docs/models/V1beta1GetProjectResourceResponse.md)
 - [V1beta1GetProjectResponse](docs/models/V1beta1GetProjectResponse.md)
 - [V1beta1GetRelationResponse](docs/models/V1beta1GetRelationResponse.md)
 - [V1beta1GetServiceUserKeyResponse](docs/models/V1beta1GetServiceUserKeyResponse.md)
 - [V1beta1GetServiceUserResponse](docs/models/V1beta1GetServiceUserResponse.md)
 - [V1beta1GetUserResponse](docs/models/V1beta1GetUserResponse.md)
 - [V1beta1Group](docs/models/V1beta1Group.md)
 - [V1beta1GroupRequestBody](docs/models/V1beta1GroupRequestBody.md)
 - [V1beta1Invitation](docs/models/V1beta1Invitation.md)
 - [V1beta1JSONWebKey](docs/models/V1beta1JSONWebKey.md)
 - [V1beta1KeyCredential](docs/models/V1beta1KeyCredential.md)
 - [V1beta1ListAllOrganizationsResponse](docs/models/V1beta1ListAllOrganizationsResponse.md)
 - [V1beta1ListAllUsersResponse](docs/models/V1beta1ListAllUsersResponse.md)
 - [V1beta1ListAuthStrategiesResponse](docs/models/V1beta1ListAuthStrategiesResponse.md)
 - [V1beta1ListCurrentUserGroupsResponse](docs/models/V1beta1ListCurrentUserGroupsResponse.md)
 - [V1beta1ListGroupUsersResponse](docs/models/V1beta1ListGroupUsersResponse.md)
 - [V1beta1ListGroupsResponse](docs/models/V1beta1ListGroupsResponse.md)
 - [V1beta1ListMetaSchemasResponse](docs/models/V1beta1ListMetaSchemasResponse.md)
 - [V1beta1ListNamespacesResponse](docs/models/V1beta1ListNamespacesResponse.md)
 - [V1beta1ListOrganizationAdminsResponse](docs/models/V1beta1ListOrganizationAdminsResponse.md)
 - [V1beta1ListOrganizationGroupsResponse](docs/models/V1beta1ListOrganizationGroupsResponse.md)
 - [V1beta1ListOrganizationInvitationsResponse](docs/models/V1beta1ListOrganizationInvitationsResponse.md)
 - [V1beta1ListOrganizationProjectsResponse](docs/models/V1beta1ListOrganizationProjectsResponse.md)
 - [V1beta1ListOrganizationRolesResponse](docs/models/V1beta1ListOrganizationRolesResponse.md)
 - [V1beta1ListOrganizationUsersResponse](docs/models/V1beta1ListOrganizationUsersResponse.md)
 - [V1beta1ListOrganizationsResponse](docs/models/V1beta1ListOrganizationsResponse.md)
 - [V1beta1ListPermissionsResponse](docs/models/V1beta1ListPermissionsResponse.md)
 - [V1beta1ListPoliciesResponse](docs/models/V1beta1ListPoliciesResponse.md)
 - [V1beta1ListProjectAdminsResponse](docs/models/V1beta1ListProjectAdminsResponse.md)
 - [V1beta1ListProjectResourcesResponse](docs/models/V1beta1ListProjectResourcesResponse.md)
 - [V1beta1ListProjectUsersResponse](docs/models/V1beta1ListProjectUsersResponse.md)
 - [V1beta1ListProjectsResponse](docs/models/V1beta1ListProjectsResponse.md)
 - [V1beta1ListRelationsResponse](docs/models/V1beta1ListRelationsResponse.md)
 - [V1beta1ListResourcesResponse](docs/models/V1beta1ListResourcesResponse.md)
 - [V1beta1ListRolesResponse](docs/models/V1beta1ListRolesResponse.md)
 - [V1beta1ListServiceUserKeysResponse](docs/models/V1beta1ListServiceUserKeysResponse.md)
 - [V1beta1ListServiceUserSecretsResponse](docs/models/V1beta1ListServiceUserSecretsResponse.md)
 - [V1beta1ListServiceUsersResponse](docs/models/V1beta1ListServiceUsersResponse.md)
 - [V1beta1ListUserGroupsResponse](docs/models/V1beta1ListUserGroupsResponse.md)
 - [V1beta1ListUserInvitationsResponse](docs/models/V1beta1ListUserInvitationsResponse.md)
 - [V1beta1ListUsersResponse](docs/models/V1beta1ListUsersResponse.md)
 - [V1beta1MetaSchema](docs/models/V1beta1MetaSchema.md)
 - [V1beta1MetaSchemaRequestBody](docs/models/V1beta1MetaSchemaRequestBody.md)
 - [V1beta1Namespace](docs/models/V1beta1Namespace.md)
 - [V1beta1Organization](docs/models/V1beta1Organization.md)
 - [V1beta1OrganizationRequestBody](docs/models/V1beta1OrganizationRequestBody.md)
 - [V1beta1Permission](docs/models/V1beta1Permission.md)
 - [V1beta1PermissionRequestBody](docs/models/V1beta1PermissionRequestBody.md)
 - [V1beta1Policy](docs/models/V1beta1Policy.md)
 - [V1beta1PolicyRequestBody](docs/models/V1beta1PolicyRequestBody.md)
 - [V1beta1Project](docs/models/V1beta1Project.md)
 - [V1beta1ProjectRequestBody](docs/models/V1beta1ProjectRequestBody.md)
 - [V1beta1Relation](docs/models/V1beta1Relation.md)
 - [V1beta1RelationRequestBody](docs/models/V1beta1RelationRequestBody.md)
 - [V1beta1Resource](docs/models/V1beta1Resource.md)
 - [V1beta1ResourceRequestBody](docs/models/V1beta1ResourceRequestBody.md)
 - [V1beta1Role](docs/models/V1beta1Role.md)
 - [V1beta1RoleRequestBody](docs/models/V1beta1RoleRequestBody.md)
 - [V1beta1SecretCredential](docs/models/V1beta1SecretCredential.md)
 - [V1beta1ServiceUser](docs/models/V1beta1ServiceUser.md)
 - [V1beta1ServiceUserKey](docs/models/V1beta1ServiceUserKey.md)
 - [V1beta1ServiceUserRequestBody](docs/models/V1beta1ServiceUserRequestBody.md)
 - [V1beta1UpdateCurrentUserResponse](docs/models/V1beta1UpdateCurrentUserResponse.md)
 - [V1beta1UpdateGroupResponse](docs/models/V1beta1UpdateGroupResponse.md)
 - [V1beta1UpdateMetaSchemaResponse](docs/models/V1beta1UpdateMetaSchemaResponse.md)
 - [V1beta1UpdateOrganizationResponse](docs/models/V1beta1UpdateOrganizationResponse.md)
 - [V1beta1UpdateOrganizationRoleResponse](docs/models/V1beta1UpdateOrganizationRoleResponse.md)
 - [V1beta1UpdatePermissionResponse](docs/models/V1beta1UpdatePermissionResponse.md)
 - [V1beta1UpdatePolicyResponse](docs/models/V1beta1UpdatePolicyResponse.md)
 - [V1beta1UpdateProjectResourceResponse](docs/models/V1beta1UpdateProjectResourceResponse.md)
 - [V1beta1UpdateProjectResponse](docs/models/V1beta1UpdateProjectResponse.md)
 - [V1beta1UpdateUserResponse](docs/models/V1beta1UpdateUserResponse.md)
 - [V1beta1User](docs/models/V1beta1User.md)
 - [V1beta1UserRequestBody](docs/models/V1beta1UserRequestBody.md)