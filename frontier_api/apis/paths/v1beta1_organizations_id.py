from frontier_api.paths.v1beta1_organizations_id.get import ApiForget
from frontier_api.paths.v1beta1_organizations_id.put import ApiForput
from frontier_api.paths.v1beta1_organizations_id.delete import ApiFordelete


class V1beta1OrganizationsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
