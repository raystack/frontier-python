from shield_api.paths.v1beta1_meta_schemas_id.get import ApiForget
from shield_api.paths.v1beta1_meta_schemas_id.put import ApiForput
from shield_api.paths.v1beta1_meta_schemas_id.delete import ApiFordelete


class V1beta1MetaSchemasId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
