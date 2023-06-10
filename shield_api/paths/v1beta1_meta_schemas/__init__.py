# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from shield_api.paths.v1beta1_meta_schemas import Api

from shield_api.paths import PathValues

path = PathValues.V1BETA1_META_SCHEMAS