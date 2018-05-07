from .BaseVO import BaseVO


class TsContractInterface(BaseVO):
    """
        契约接口表(ts_contract_interface)对应的VO对象
    """

    def __init__(self, ukid, name, ppt_relation_ukid,
                 business_unit_ukid, start_time, status, create_time, update_time):
        BaseVO.__init__(self)
        self.ukid = ukid
        self.name = name
        self.ppt_relation_ukid = ppt_relation_ukid
        self.business_unit_ukid = business_unit_ukid
        self.start_time = start_time
        self.status = status
        self.create_time = create_time
        self.update_time = update_time
