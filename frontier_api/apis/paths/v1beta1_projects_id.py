from frontier_api.paths.v1beta1_projects_id.get import ApiForget
from frontier_api.paths.v1beta1_projects_id.put import ApiForput
from frontier_api.paths.v1beta1_projects_id.delete import ApiFordelete


class V1beta1ProjectsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
