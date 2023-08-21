import typing_extensions

from frontier_api.apis.tags import TagValues
from frontier_api.apis.tags.admin_service_api import AdminServiceApi
from frontier_api.apis.tags.frontier_service_api import FrontierServiceApi
from frontier_api.apis.tags.user_api import UserApi
from frontier_api.apis.tags.group_api import GroupApi
from frontier_api.apis.tags.organization_api import OrganizationApi
from frontier_api.apis.tags.project_api import ProjectApi
from frontier_api.apis.tags.relation_api import RelationApi
from frontier_api.apis.tags.resource_api import ResourceApi
from frontier_api.apis.tags.policy_api import PolicyApi
from frontier_api.apis.tags.role_api import RoleApi
from frontier_api.apis.tags.permission_api import PermissionApi
from frontier_api.apis.tags.audit_log_api import AuditLogApi
from frontier_api.apis.tags.authn_api import AuthnApi
from frontier_api.apis.tags.authz_api import AuthzApi
from frontier_api.apis.tags.meta_schema_api import MetaSchemaApi
from frontier_api.apis.tags.namespace_api import NamespaceApi
from frontier_api.apis.tags.preference_api import PreferenceApi
from frontier_api.apis.tags.service_user_api import ServiceUserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ADMIN_SERVICE: AdminServiceApi,
        TagValues.FRONTIER_SERVICE: FrontierServiceApi,
        TagValues.USER: UserApi,
        TagValues.GROUP: GroupApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.RELATION: RelationApi,
        TagValues.RESOURCE: ResourceApi,
        TagValues.POLICY: PolicyApi,
        TagValues.ROLE: RoleApi,
        TagValues.PERMISSION: PermissionApi,
        TagValues.AUDIT_LOG: AuditLogApi,
        TagValues.AUTHN: AuthnApi,
        TagValues.AUTHZ: AuthzApi,
        TagValues.META_SCHEMA: MetaSchemaApi,
        TagValues.NAMESPACE: NamespaceApi,
        TagValues.PREFERENCE: PreferenceApi,
        TagValues.SERVICE_USER: ServiceUserApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ADMIN_SERVICE: AdminServiceApi,
        TagValues.FRONTIER_SERVICE: FrontierServiceApi,
        TagValues.USER: UserApi,
        TagValues.GROUP: GroupApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.RELATION: RelationApi,
        TagValues.RESOURCE: ResourceApi,
        TagValues.POLICY: PolicyApi,
        TagValues.ROLE: RoleApi,
        TagValues.PERMISSION: PermissionApi,
        TagValues.AUDIT_LOG: AuditLogApi,
        TagValues.AUTHN: AuthnApi,
        TagValues.AUTHZ: AuthzApi,
        TagValues.META_SCHEMA: MetaSchemaApi,
        TagValues.NAMESPACE: NamespaceApi,
        TagValues.PREFERENCE: PreferenceApi,
        TagValues.SERVICE_USER: ServiceUserApi,
    }
)
