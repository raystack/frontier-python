# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from frontier_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    _WELLKNOWN_JWKS_JSON = "/.well-known/jwks.json"
    V1BETA1_ADMIN_GROUPS = "/v1beta1/admin/groups"
    V1BETA1_ADMIN_ORGANIZATIONS = "/v1beta1/admin/organizations"
    V1BETA1_ADMIN_PROJECTS = "/v1beta1/admin/projects"
    V1BETA1_ADMIN_RELATIONS = "/v1beta1/admin/relations"
    V1BETA1_ADMIN_RESOURCES = "/v1beta1/admin/resources"
    V1BETA1_ADMIN_USERS = "/v1beta1/admin/users"
    V1BETA1_AUTH = "/v1beta1/auth"
    V1BETA1_AUTH_CALLBACK = "/v1beta1/auth/callback"
    V1BETA1_AUTH_JWKS = "/v1beta1/auth/jwks"
    V1BETA1_AUTH_LOGOUT = "/v1beta1/auth/logout"
    V1BETA1_AUTH_REGISTER_STRATEGY_NAME = "/v1beta1/auth/register/{strategyName}"
    V1BETA1_AUTH_TOKEN = "/v1beta1/auth/token"
    V1BETA1_CHECK = "/v1beta1/check"
    V1BETA1_GROUPS_ID_PREFERENCES = "/v1beta1/groups/{id}/preferences"
    V1BETA1_META_SCHEMAS = "/v1beta1/meta/schemas"
    V1BETA1_META_SCHEMAS_ID = "/v1beta1/meta/schemas/{id}"
    V1BETA1_NAMESPACES = "/v1beta1/namespaces"
    V1BETA1_NAMESPACES_ID = "/v1beta1/namespaces/{id}"
    V1BETA1_ORGANIZATION_ORG_ID_AUDITLOGS = "/v1beta1/organization/{orgId}/auditlogs"
    V1BETA1_ORGANIZATION_ORG_ID_AUDITLOGS_ID = "/v1beta1/organization/{orgId}/auditlogs/{id}"
    V1BETA1_ORGANIZATIONS = "/v1beta1/organizations"
    V1BETA1_ORGANIZATIONS_ID = "/v1beta1/organizations/{id}"
    V1BETA1_ORGANIZATIONS_ID_ADMINS = "/v1beta1/organizations/{id}/admins"
    V1BETA1_ORGANIZATIONS_ID_DISABLE = "/v1beta1/organizations/{id}/disable"
    V1BETA1_ORGANIZATIONS_ID_ENABLE = "/v1beta1/organizations/{id}/enable"
    V1BETA1_ORGANIZATIONS_ID_PREFERENCES = "/v1beta1/organizations/{id}/preferences"
    V1BETA1_ORGANIZATIONS_ID_PROJECTS = "/v1beta1/organizations/{id}/projects"
    V1BETA1_ORGANIZATIONS_ID_SERVICEUSERS = "/v1beta1/organizations/{id}/serviceusers"
    V1BETA1_ORGANIZATIONS_ID_USERS = "/v1beta1/organizations/{id}/users"
    V1BETA1_ORGANIZATIONS_ID_USERS_USER_ID = "/v1beta1/organizations/{id}/users/{userId}"
    V1BETA1_ORGANIZATIONS_ORG_ID_DOMAINS = "/v1beta1/organizations/{orgId}/domains"
    V1BETA1_ORGANIZATIONS_ORG_ID_DOMAINS_ID = "/v1beta1/organizations/{orgId}/domains/{id}"
    V1BETA1_ORGANIZATIONS_ORG_ID_DOMAINS_ID_VERIFY = "/v1beta1/organizations/{orgId}/domains/{id}/verify"
    V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS = "/v1beta1/organizations/{orgId}/groups"
    V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID = "/v1beta1/organizations/{orgId}/groups/{id}"
    V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_DISABLE = "/v1beta1/organizations/{orgId}/groups/{id}/disable"
    V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_ENABLE = "/v1beta1/organizations/{orgId}/groups/{id}/enable"
    V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_USERS = "/v1beta1/organizations/{orgId}/groups/{id}/users"
    V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_USERS_USER_ID = "/v1beta1/organizations/{orgId}/groups/{id}/users/{userId}"
    V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS = "/v1beta1/organizations/{orgId}/invitations"
    V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS_ID = "/v1beta1/organizations/{orgId}/invitations/{id}"
    V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS_ID_ACCEPT = "/v1beta1/organizations/{orgId}/invitations/{id}/accept"
    V1BETA1_ORGANIZATIONS_ORG_ID_JOIN = "/v1beta1/organizations/{orgId}/join"
    V1BETA1_ORGANIZATIONS_ORG_ID_ROLES = "/v1beta1/organizations/{orgId}/roles"
    V1BETA1_ORGANIZATIONS_ORG_ID_ROLES_ID = "/v1beta1/organizations/{orgId}/roles/{id}"
    V1BETA1_PERMISSIONS = "/v1beta1/permissions"
    V1BETA1_PERMISSIONS_ID = "/v1beta1/permissions/{id}"
    V1BETA1_POLICIES = "/v1beta1/policies"
    V1BETA1_POLICIES_ID = "/v1beta1/policies/{id}"
    V1BETA1_PREFERENCES = "/v1beta1/preferences"
    V1BETA1_PREFERENCES_TRAITS = "/v1beta1/preferences/traits"
    V1BETA1_PROJECTS = "/v1beta1/projects"
    V1BETA1_PROJECTS_ID = "/v1beta1/projects/{id}"
    V1BETA1_PROJECTS_ID_ADMINS = "/v1beta1/projects/{id}/admins"
    V1BETA1_PROJECTS_ID_DISABLE = "/v1beta1/projects/{id}/disable"
    V1BETA1_PROJECTS_ID_ENABLE = "/v1beta1/projects/{id}/enable"
    V1BETA1_PROJECTS_ID_PREFERENCES = "/v1beta1/projects/{id}/preferences"
    V1BETA1_PROJECTS_ID_USERS = "/v1beta1/projects/{id}/users"
    V1BETA1_PROJECTS_PROJECT_ID_RESOURCES = "/v1beta1/projects/{projectId}/resources"
    V1BETA1_PROJECTS_PROJECT_ID_RESOURCES_ID = "/v1beta1/projects/{projectId}/resources/{id}"
    V1BETA1_RELATIONS = "/v1beta1/relations"
    V1BETA1_RELATIONS_ID = "/v1beta1/relations/{id}"
    V1BETA1_RELATIONS_RELATION_OBJECT_OBJECT_SUBJECT_SUBJECT = "/v1beta1/relations/{relation}/object/{object}/subject/{subject}"
    V1BETA1_ROLES = "/v1beta1/roles"
    V1BETA1_ROLES_ID = "/v1beta1/roles/{id}"
    V1BETA1_SERVICEUSERS = "/v1beta1/serviceusers"
    V1BETA1_SERVICEUSERS_ID = "/v1beta1/serviceusers/{id}"
    V1BETA1_SERVICEUSERS_ID_KEYS = "/v1beta1/serviceusers/{id}/keys"
    V1BETA1_SERVICEUSERS_ID_KEYS_KEY_ID = "/v1beta1/serviceusers/{id}/keys/{keyId}"
    V1BETA1_SERVICEUSERS_ID_SECRETS = "/v1beta1/serviceusers/{id}/secrets"
    V1BETA1_SERVICEUSERS_ID_SECRETS_SECRET_ID = "/v1beta1/serviceusers/{id}/secrets/{secretId}"
    V1BETA1_USERS = "/v1beta1/users"
    V1BETA1_USERS_ID = "/v1beta1/users/{id}"
    V1BETA1_USERS_ID_DISABLE = "/v1beta1/users/{id}/disable"
    V1BETA1_USERS_ID_ENABLE = "/v1beta1/users/{id}/enable"
    V1BETA1_USERS_ID_GROUPS = "/v1beta1/users/{id}/groups"
    V1BETA1_USERS_ID_INVITATIONS = "/v1beta1/users/{id}/invitations"
    V1BETA1_USERS_ID_ORGANIZATIONS = "/v1beta1/users/{id}/organizations"
    V1BETA1_USERS_ID_PREFERENCES = "/v1beta1/users/{id}/preferences"
    V1BETA1_USERS_ID_PROJECTS = "/v1beta1/users/{id}/projects"
    V1BETA1_USERS_SELF = "/v1beta1/users/self"
    V1BETA1_USERS_SELF_GROUPS = "/v1beta1/users/self/groups"
    V1BETA1_USERS_SELF_ORGANIZATIONS = "/v1beta1/users/self/organizations"
    V1BETA1_USERS_SELF_PREFERENCES = "/v1beta1/users/self/preferences"
    V1BETA1_USERS_SELF_PROJECTS = "/v1beta1/users/self/projects"
