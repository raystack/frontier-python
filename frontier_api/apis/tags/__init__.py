# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from frontier_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ADMIN_SERVICE = "AdminService"
    FRONTIER_SERVICE = "FrontierService"
    USER = "User"
    GROUP = "Group"
    ORGANIZATION = "Organization"
    PROJECT = "Project"
    RELATION = "Relation"
    RESOURCE = "Resource"
    POLICY = "Policy"
    ROLE = "Role"
    PERMISSION = "Permission"
    AUDIT_LOG = "AuditLog"
    AUTHN = "Authn"
    AUTHZ = "Authz"
    META_SCHEMA = "MetaSchema"
    NAMESPACE = "Namespace"
    SERVICE_USER = "ServiceUser"
