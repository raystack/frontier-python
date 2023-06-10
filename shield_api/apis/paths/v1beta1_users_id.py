from shield_api.paths.v1beta1_users_id.get import ApiForget
from shield_api.paths.v1beta1_users_id.put import ApiForput
from shield_api.paths.v1beta1_users_id.delete import ApiFordelete


class V1beta1UsersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
