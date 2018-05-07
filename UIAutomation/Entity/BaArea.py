from UIAutomation.Entity import BaseVO


class BaArea(BaseVO):
    """
        地区信息表(ba_area)对应的VO对象
    """

    def __init__(self, country_id, area_id, area_name, parent_area_id,
                 area_level, user_id_updated, date_updated,
                 program_id, workstation_id):
        BaseVO.__init__(self)
        self.country_id = country_id
        self.area_id = area_id
        self.area_name = area_name
        self.parent_area_id = parent_area_id
        self.area_level = area_level
        self.user_id_updated = user_id_updated
        self.date_updated = date_updated
        self.program_id = program_id
        self.workstation_id = workstation_id
