from frontier_api.paths.v1beta1_permissions_id.get import ApiForget
from frontier_api.paths.v1beta1_permissions_id.put import ApiForput
from frontier_api.paths.v1beta1_permissions_id.delete import ApiFordelete


class V1beta1PermissionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass