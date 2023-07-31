from frontier_api.paths.v1beta1_policies_id.get import ApiForget
from frontier_api.paths.v1beta1_policies_id.put import ApiForput
from frontier_api.paths.v1beta1_policies_id.delete import ApiFordelete


class V1beta1PoliciesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
