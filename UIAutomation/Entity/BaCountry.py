from .BaseVO import BaseVO


class BaCountry(BaseVO):
    """
        国家信息表(ba_country)对应的VO对象
    """

    def __init__(self, country_id, country_name_en, country_name_zh,
                 country_calling_code, time_zone, jet_lag, extra_country_id):
        BaseVO.__init__(self)
        self.country_id = country_id
        self.country_name_en = country_name_en
        self.country_name_zh = country_name_zh
        self.country_calling_code = country_calling_code
        self.time_zone = time_zone
        self.jet_lag = jet_lag
        self.extra_country_id = extra_country_id
