import typing_extensions

from shield_api.paths import PathValues
from shield_api.apis.paths.well_known_jwks_json import WellKnownJwksJson
from shield_api.apis.paths.v1beta1_admin_groups import V1beta1AdminGroups
from shield_api.apis.paths.v1beta1_admin_organizations import V1beta1AdminOrganizations
from shield_api.apis.paths.v1beta1_admin_projects import V1beta1AdminProjects
from shield_api.apis.paths.v1beta1_admin_relations import V1beta1AdminRelations
from shield_api.apis.paths.v1beta1_admin_resources import V1beta1AdminResources
from shield_api.apis.paths.v1beta1_admin_users import V1beta1AdminUsers
from shield_api.apis.paths.v1beta1_auth import V1beta1Auth
from shield_api.apis.paths.v1beta1_auth_callback import V1beta1AuthCallback
from shield_api.apis.paths.v1beta1_auth_jwks import V1beta1AuthJwks
from shield_api.apis.paths.v1beta1_auth_logout import V1beta1AuthLogout
from shield_api.apis.paths.v1beta1_auth_register_strategy_name import V1beta1AuthRegisterStrategyName
from shield_api.apis.paths.v1beta1_auth_token import V1beta1AuthToken
from shield_api.apis.paths.v1beta1_check import V1beta1Check
from shield_api.apis.paths.v1beta1_meta_schemas import V1beta1MetaSchemas
from shield_api.apis.paths.v1beta1_meta_schemas_id import V1beta1MetaSchemasId
from shield_api.apis.paths.v1beta1_namespaces import V1beta1Namespaces
from shield_api.apis.paths.v1beta1_namespaces_id import V1beta1NamespacesId
from shield_api.apis.paths.v1beta1_organization_org_id_auditlogs import V1beta1OrganizationOrgIdAuditlogs
from shield_api.apis.paths.v1beta1_organization_org_id_auditlogs_id import V1beta1OrganizationOrgIdAuditlogsId
from shield_api.apis.paths.v1beta1_organizations import V1beta1Organizations
from shield_api.apis.paths.v1beta1_organizations_id import V1beta1OrganizationsId
from shield_api.apis.paths.v1beta1_organizations_id_admins import V1beta1OrganizationsIdAdmins
from shield_api.apis.paths.v1beta1_organizations_id_disable import V1beta1OrganizationsIdDisable
from shield_api.apis.paths.v1beta1_organizations_id_enable import V1beta1OrganizationsIdEnable
from shield_api.apis.paths.v1beta1_organizations_id_projects import V1beta1OrganizationsIdProjects
from shield_api.apis.paths.v1beta1_organizations_id_serviceusers import V1beta1OrganizationsIdServiceusers
from shield_api.apis.paths.v1beta1_organizations_id_users import V1beta1OrganizationsIdUsers
from shield_api.apis.paths.v1beta1_organizations_id_users_user_id import V1beta1OrganizationsIdUsersUserId
from shield_api.apis.paths.v1beta1_organizations_org_id_groups import V1beta1OrganizationsOrgIdGroups
from shield_api.apis.paths.v1beta1_organizations_org_id_groups_id import V1beta1OrganizationsOrgIdGroupsId
from shield_api.apis.paths.v1beta1_organizations_org_id_groups_id_disable import V1beta1OrganizationsOrgIdGroupsIdDisable
from shield_api.apis.paths.v1beta1_organizations_org_id_groups_id_enable import V1beta1OrganizationsOrgIdGroupsIdEnable
from shield_api.apis.paths.v1beta1_organizations_org_id_groups_id_users import V1beta1OrganizationsOrgIdGroupsIdUsers
from shield_api.apis.paths.v1beta1_organizations_org_id_groups_id_users_user_id import V1beta1OrganizationsOrgIdGroupsIdUsersUserId
from shield_api.apis.paths.v1beta1_organizations_org_id_invitations import V1beta1OrganizationsOrgIdInvitations
from shield_api.apis.paths.v1beta1_organizations_org_id_invitations_id import V1beta1OrganizationsOrgIdInvitationsId
from shield_api.apis.paths.v1beta1_organizations_org_id_invitations_id_accept import V1beta1OrganizationsOrgIdInvitationsIdAccept
from shield_api.apis.paths.v1beta1_organizations_org_id_roles import V1beta1OrganizationsOrgIdRoles
from shield_api.apis.paths.v1beta1_organizations_org_id_roles_id import V1beta1OrganizationsOrgIdRolesId
from shield_api.apis.paths.v1beta1_permissions import V1beta1Permissions
from shield_api.apis.paths.v1beta1_permissions_id import V1beta1PermissionsId
from shield_api.apis.paths.v1beta1_policies import V1beta1Policies
from shield_api.apis.paths.v1beta1_policies_id import V1beta1PoliciesId
from shield_api.apis.paths.v1beta1_projects import V1beta1Projects
from shield_api.apis.paths.v1beta1_projects_id import V1beta1ProjectsId
from shield_api.apis.paths.v1beta1_projects_id_admins import V1beta1ProjectsIdAdmins
from shield_api.apis.paths.v1beta1_projects_id_disable import V1beta1ProjectsIdDisable
from shield_api.apis.paths.v1beta1_projects_id_enable import V1beta1ProjectsIdEnable
from shield_api.apis.paths.v1beta1_projects_id_users import V1beta1ProjectsIdUsers
from shield_api.apis.paths.v1beta1_projects_project_id_resources import V1beta1ProjectsProjectIdResources
from shield_api.apis.paths.v1beta1_projects_project_id_resources_id import V1beta1ProjectsProjectIdResourcesId
from shield_api.apis.paths.v1beta1_relations import V1beta1Relations
from shield_api.apis.paths.v1beta1_relations_id import V1beta1RelationsId
from shield_api.apis.paths.v1beta1_relations_relation_object_object_subject_subject import V1beta1RelationsRelationObjectObjectSubjectSubject
from shield_api.apis.paths.v1beta1_roles import V1beta1Roles
from shield_api.apis.paths.v1beta1_roles_id import V1beta1RolesId
from shield_api.apis.paths.v1beta1_serviceusers import V1beta1Serviceusers
from shield_api.apis.paths.v1beta1_serviceusers_id import V1beta1ServiceusersId
from shield_api.apis.paths.v1beta1_serviceusers_id_keys import V1beta1ServiceusersIdKeys
from shield_api.apis.paths.v1beta1_serviceusers_id_keys_key_id import V1beta1ServiceusersIdKeysKeyId
from shield_api.apis.paths.v1beta1_serviceusers_id_secrets import V1beta1ServiceusersIdSecrets
from shield_api.apis.paths.v1beta1_serviceusers_id_secrets_secret_id import V1beta1ServiceusersIdSecretsSecretId
from shield_api.apis.paths.v1beta1_users import V1beta1Users
from shield_api.apis.paths.v1beta1_users_id import V1beta1UsersId
from shield_api.apis.paths.v1beta1_users_id_disable import V1beta1UsersIdDisable
from shield_api.apis.paths.v1beta1_users_id_enable import V1beta1UsersIdEnable
from shield_api.apis.paths.v1beta1_users_id_groups import V1beta1UsersIdGroups
from shield_api.apis.paths.v1beta1_users_id_invitations import V1beta1UsersIdInvitations
from shield_api.apis.paths.v1beta1_users_id_organizations import V1beta1UsersIdOrganizations
from shield_api.apis.paths.v1beta1_users_id_projects import V1beta1UsersIdProjects
from shield_api.apis.paths.v1beta1_users_self import V1beta1UsersSelf
from shield_api.apis.paths.v1beta1_users_self_groups import V1beta1UsersSelfGroups
from shield_api.apis.paths.v1beta1_users_self_organizations import V1beta1UsersSelfOrganizations
from shield_api.apis.paths.v1beta1_users_self_projects import V1beta1UsersSelfProjects

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues._WELLKNOWN_JWKS_JSON: WellKnownJwksJson,
        PathValues.V1BETA1_ADMIN_GROUPS: V1beta1AdminGroups,
        PathValues.V1BETA1_ADMIN_ORGANIZATIONS: V1beta1AdminOrganizations,
        PathValues.V1BETA1_ADMIN_PROJECTS: V1beta1AdminProjects,
        PathValues.V1BETA1_ADMIN_RELATIONS: V1beta1AdminRelations,
        PathValues.V1BETA1_ADMIN_RESOURCES: V1beta1AdminResources,
        PathValues.V1BETA1_ADMIN_USERS: V1beta1AdminUsers,
        PathValues.V1BETA1_AUTH: V1beta1Auth,
        PathValues.V1BETA1_AUTH_CALLBACK: V1beta1AuthCallback,
        PathValues.V1BETA1_AUTH_JWKS: V1beta1AuthJwks,
        PathValues.V1BETA1_AUTH_LOGOUT: V1beta1AuthLogout,
        PathValues.V1BETA1_AUTH_REGISTER_STRATEGY_NAME: V1beta1AuthRegisterStrategyName,
        PathValues.V1BETA1_AUTH_TOKEN: V1beta1AuthToken,
        PathValues.V1BETA1_CHECK: V1beta1Check,
        PathValues.V1BETA1_META_SCHEMAS: V1beta1MetaSchemas,
        PathValues.V1BETA1_META_SCHEMAS_ID: V1beta1MetaSchemasId,
        PathValues.V1BETA1_NAMESPACES: V1beta1Namespaces,
        PathValues.V1BETA1_NAMESPACES_ID: V1beta1NamespacesId,
        PathValues.V1BETA1_ORGANIZATION_ORG_ID_AUDITLOGS: V1beta1OrganizationOrgIdAuditlogs,
        PathValues.V1BETA1_ORGANIZATION_ORG_ID_AUDITLOGS_ID: V1beta1OrganizationOrgIdAuditlogsId,
        PathValues.V1BETA1_ORGANIZATIONS: V1beta1Organizations,
        PathValues.V1BETA1_ORGANIZATIONS_ID: V1beta1OrganizationsId,
        PathValues.V1BETA1_ORGANIZATIONS_ID_ADMINS: V1beta1OrganizationsIdAdmins,
        PathValues.V1BETA1_ORGANIZATIONS_ID_DISABLE: V1beta1OrganizationsIdDisable,
        PathValues.V1BETA1_ORGANIZATIONS_ID_ENABLE: V1beta1OrganizationsIdEnable,
        PathValues.V1BETA1_ORGANIZATIONS_ID_PROJECTS: V1beta1OrganizationsIdProjects,
        PathValues.V1BETA1_ORGANIZATIONS_ID_SERVICEUSERS: V1beta1OrganizationsIdServiceusers,
        PathValues.V1BETA1_ORGANIZATIONS_ID_USERS: V1beta1OrganizationsIdUsers,
        PathValues.V1BETA1_ORGANIZATIONS_ID_USERS_USER_ID: V1beta1OrganizationsIdUsersUserId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS: V1beta1OrganizationsOrgIdGroups,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID: V1beta1OrganizationsOrgIdGroupsId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_DISABLE: V1beta1OrganizationsOrgIdGroupsIdDisable,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_ENABLE: V1beta1OrganizationsOrgIdGroupsIdEnable,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_USERS: V1beta1OrganizationsOrgIdGroupsIdUsers,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_USERS_USER_ID: V1beta1OrganizationsOrgIdGroupsIdUsersUserId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS: V1beta1OrganizationsOrgIdInvitations,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS_ID: V1beta1OrganizationsOrgIdInvitationsId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS_ID_ACCEPT: V1beta1OrganizationsOrgIdInvitationsIdAccept,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_ROLES: V1beta1OrganizationsOrgIdRoles,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_ROLES_ID: V1beta1OrganizationsOrgIdRolesId,
        PathValues.V1BETA1_PERMISSIONS: V1beta1Permissions,
        PathValues.V1BETA1_PERMISSIONS_ID: V1beta1PermissionsId,
        PathValues.V1BETA1_POLICIES: V1beta1Policies,
        PathValues.V1BETA1_POLICIES_ID: V1beta1PoliciesId,
        PathValues.V1BETA1_PROJECTS: V1beta1Projects,
        PathValues.V1BETA1_PROJECTS_ID: V1beta1ProjectsId,
        PathValues.V1BETA1_PROJECTS_ID_ADMINS: V1beta1ProjectsIdAdmins,
        PathValues.V1BETA1_PROJECTS_ID_DISABLE: V1beta1ProjectsIdDisable,
        PathValues.V1BETA1_PROJECTS_ID_ENABLE: V1beta1ProjectsIdEnable,
        PathValues.V1BETA1_PROJECTS_ID_USERS: V1beta1ProjectsIdUsers,
        PathValues.V1BETA1_PROJECTS_PROJECT_ID_RESOURCES: V1beta1ProjectsProjectIdResources,
        PathValues.V1BETA1_PROJECTS_PROJECT_ID_RESOURCES_ID: V1beta1ProjectsProjectIdResourcesId,
        PathValues.V1BETA1_RELATIONS: V1beta1Relations,
        PathValues.V1BETA1_RELATIONS_ID: V1beta1RelationsId,
        PathValues.V1BETA1_RELATIONS_RELATION_OBJECT_OBJECT_SUBJECT_SUBJECT: V1beta1RelationsRelationObjectObjectSubjectSubject,
        PathValues.V1BETA1_ROLES: V1beta1Roles,
        PathValues.V1BETA1_ROLES_ID: V1beta1RolesId,
        PathValues.V1BETA1_SERVICEUSERS: V1beta1Serviceusers,
        PathValues.V1BETA1_SERVICEUSERS_ID: V1beta1ServiceusersId,
        PathValues.V1BETA1_SERVICEUSERS_ID_KEYS: V1beta1ServiceusersIdKeys,
        PathValues.V1BETA1_SERVICEUSERS_ID_KEYS_KEY_ID: V1beta1ServiceusersIdKeysKeyId,
        PathValues.V1BETA1_SERVICEUSERS_ID_SECRETS: V1beta1ServiceusersIdSecrets,
        PathValues.V1BETA1_SERVICEUSERS_ID_SECRETS_SECRET_ID: V1beta1ServiceusersIdSecretsSecretId,
        PathValues.V1BETA1_USERS: V1beta1Users,
        PathValues.V1BETA1_USERS_ID: V1beta1UsersId,
        PathValues.V1BETA1_USERS_ID_DISABLE: V1beta1UsersIdDisable,
        PathValues.V1BETA1_USERS_ID_ENABLE: V1beta1UsersIdEnable,
        PathValues.V1BETA1_USERS_ID_GROUPS: V1beta1UsersIdGroups,
        PathValues.V1BETA1_USERS_ID_INVITATIONS: V1beta1UsersIdInvitations,
        PathValues.V1BETA1_USERS_ID_ORGANIZATIONS: V1beta1UsersIdOrganizations,
        PathValues.V1BETA1_USERS_ID_PROJECTS: V1beta1UsersIdProjects,
        PathValues.V1BETA1_USERS_SELF: V1beta1UsersSelf,
        PathValues.V1BETA1_USERS_SELF_GROUPS: V1beta1UsersSelfGroups,
        PathValues.V1BETA1_USERS_SELF_ORGANIZATIONS: V1beta1UsersSelfOrganizations,
        PathValues.V1BETA1_USERS_SELF_PROJECTS: V1beta1UsersSelfProjects,
    }
)

path_to_api = PathToApi(
    {
        PathValues._WELLKNOWN_JWKS_JSON: WellKnownJwksJson,
        PathValues.V1BETA1_ADMIN_GROUPS: V1beta1AdminGroups,
        PathValues.V1BETA1_ADMIN_ORGANIZATIONS: V1beta1AdminOrganizations,
        PathValues.V1BETA1_ADMIN_PROJECTS: V1beta1AdminProjects,
        PathValues.V1BETA1_ADMIN_RELATIONS: V1beta1AdminRelations,
        PathValues.V1BETA1_ADMIN_RESOURCES: V1beta1AdminResources,
        PathValues.V1BETA1_ADMIN_USERS: V1beta1AdminUsers,
        PathValues.V1BETA1_AUTH: V1beta1Auth,
        PathValues.V1BETA1_AUTH_CALLBACK: V1beta1AuthCallback,
        PathValues.V1BETA1_AUTH_JWKS: V1beta1AuthJwks,
        PathValues.V1BETA1_AUTH_LOGOUT: V1beta1AuthLogout,
        PathValues.V1BETA1_AUTH_REGISTER_STRATEGY_NAME: V1beta1AuthRegisterStrategyName,
        PathValues.V1BETA1_AUTH_TOKEN: V1beta1AuthToken,
        PathValues.V1BETA1_CHECK: V1beta1Check,
        PathValues.V1BETA1_META_SCHEMAS: V1beta1MetaSchemas,
        PathValues.V1BETA1_META_SCHEMAS_ID: V1beta1MetaSchemasId,
        PathValues.V1BETA1_NAMESPACES: V1beta1Namespaces,
        PathValues.V1BETA1_NAMESPACES_ID: V1beta1NamespacesId,
        PathValues.V1BETA1_ORGANIZATION_ORG_ID_AUDITLOGS: V1beta1OrganizationOrgIdAuditlogs,
        PathValues.V1BETA1_ORGANIZATION_ORG_ID_AUDITLOGS_ID: V1beta1OrganizationOrgIdAuditlogsId,
        PathValues.V1BETA1_ORGANIZATIONS: V1beta1Organizations,
        PathValues.V1BETA1_ORGANIZATIONS_ID: V1beta1OrganizationsId,
        PathValues.V1BETA1_ORGANIZATIONS_ID_ADMINS: V1beta1OrganizationsIdAdmins,
        PathValues.V1BETA1_ORGANIZATIONS_ID_DISABLE: V1beta1OrganizationsIdDisable,
        PathValues.V1BETA1_ORGANIZATIONS_ID_ENABLE: V1beta1OrganizationsIdEnable,
        PathValues.V1BETA1_ORGANIZATIONS_ID_PROJECTS: V1beta1OrganizationsIdProjects,
        PathValues.V1BETA1_ORGANIZATIONS_ID_SERVICEUSERS: V1beta1OrganizationsIdServiceusers,
        PathValues.V1BETA1_ORGANIZATIONS_ID_USERS: V1beta1OrganizationsIdUsers,
        PathValues.V1BETA1_ORGANIZATIONS_ID_USERS_USER_ID: V1beta1OrganizationsIdUsersUserId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS: V1beta1OrganizationsOrgIdGroups,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID: V1beta1OrganizationsOrgIdGroupsId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_DISABLE: V1beta1OrganizationsOrgIdGroupsIdDisable,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_ENABLE: V1beta1OrganizationsOrgIdGroupsIdEnable,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_USERS: V1beta1OrganizationsOrgIdGroupsIdUsers,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_GROUPS_ID_USERS_USER_ID: V1beta1OrganizationsOrgIdGroupsIdUsersUserId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS: V1beta1OrganizationsOrgIdInvitations,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS_ID: V1beta1OrganizationsOrgIdInvitationsId,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_INVITATIONS_ID_ACCEPT: V1beta1OrganizationsOrgIdInvitationsIdAccept,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_ROLES: V1beta1OrganizationsOrgIdRoles,
        PathValues.V1BETA1_ORGANIZATIONS_ORG_ID_ROLES_ID: V1beta1OrganizationsOrgIdRolesId,
        PathValues.V1BETA1_PERMISSIONS: V1beta1Permissions,
        PathValues.V1BETA1_PERMISSIONS_ID: V1beta1PermissionsId,
        PathValues.V1BETA1_POLICIES: V1beta1Policies,
        PathValues.V1BETA1_POLICIES_ID: V1beta1PoliciesId,
        PathValues.V1BETA1_PROJECTS: V1beta1Projects,
        PathValues.V1BETA1_PROJECTS_ID: V1beta1ProjectsId,
        PathValues.V1BETA1_PROJECTS_ID_ADMINS: V1beta1ProjectsIdAdmins,
        PathValues.V1BETA1_PROJECTS_ID_DISABLE: V1beta1ProjectsIdDisable,
        PathValues.V1BETA1_PROJECTS_ID_ENABLE: V1beta1ProjectsIdEnable,
        PathValues.V1BETA1_PROJECTS_ID_USERS: V1beta1ProjectsIdUsers,
        PathValues.V1BETA1_PROJECTS_PROJECT_ID_RESOURCES: V1beta1ProjectsProjectIdResources,
        PathValues.V1BETA1_PROJECTS_PROJECT_ID_RESOURCES_ID: V1beta1ProjectsProjectIdResourcesId,
        PathValues.V1BETA1_RELATIONS: V1beta1Relations,
        PathValues.V1BETA1_RELATIONS_ID: V1beta1RelationsId,
        PathValues.V1BETA1_RELATIONS_RELATION_OBJECT_OBJECT_SUBJECT_SUBJECT: V1beta1RelationsRelationObjectObjectSubjectSubject,
        PathValues.V1BETA1_ROLES: V1beta1Roles,
        PathValues.V1BETA1_ROLES_ID: V1beta1RolesId,
        PathValues.V1BETA1_SERVICEUSERS: V1beta1Serviceusers,
        PathValues.V1BETA1_SERVICEUSERS_ID: V1beta1ServiceusersId,
        PathValues.V1BETA1_SERVICEUSERS_ID_KEYS: V1beta1ServiceusersIdKeys,
        PathValues.V1BETA1_SERVICEUSERS_ID_KEYS_KEY_ID: V1beta1ServiceusersIdKeysKeyId,
        PathValues.V1BETA1_SERVICEUSERS_ID_SECRETS: V1beta1ServiceusersIdSecrets,
        PathValues.V1BETA1_SERVICEUSERS_ID_SECRETS_SECRET_ID: V1beta1ServiceusersIdSecretsSecretId,
        PathValues.V1BETA1_USERS: V1beta1Users,
        PathValues.V1BETA1_USERS_ID: V1beta1UsersId,
        PathValues.V1BETA1_USERS_ID_DISABLE: V1beta1UsersIdDisable,
        PathValues.V1BETA1_USERS_ID_ENABLE: V1beta1UsersIdEnable,
        PathValues.V1BETA1_USERS_ID_GROUPS: V1beta1UsersIdGroups,
        PathValues.V1BETA1_USERS_ID_INVITATIONS: V1beta1UsersIdInvitations,
        PathValues.V1BETA1_USERS_ID_ORGANIZATIONS: V1beta1UsersIdOrganizations,
        PathValues.V1BETA1_USERS_ID_PROJECTS: V1beta1UsersIdProjects,
        PathValues.V1BETA1_USERS_SELF: V1beta1UsersSelf,
        PathValues.V1BETA1_USERS_SELF_GROUPS: V1beta1UsersSelfGroups,
        PathValues.V1BETA1_USERS_SELF_ORGANIZATIONS: V1beta1UsersSelfOrganizations,
        PathValues.V1BETA1_USERS_SELF_PROJECTS: V1beta1UsersSelfProjects,
    }
)
