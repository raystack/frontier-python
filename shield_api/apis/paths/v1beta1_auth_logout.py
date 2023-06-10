from shield_api.paths.v1beta1_auth_logout.get import ApiForget
from shield_api.paths.v1beta1_auth_logout.delete import ApiFordelete


class V1beta1AuthLogout(
    ApiForget,
    ApiFordelete,
):
    pass
