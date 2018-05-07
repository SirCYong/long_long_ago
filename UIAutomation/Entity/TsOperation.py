from .BaseVO import BaseVO


class TsOperation(BaseVO):
    """
        任务表(ts_operation)对应的VO对象
    """

    def __init__(self, operation_ukid, status, ppt_relation_ukid, start_time,
                 end_time, pass_time,
                 service_ukid, operation_type, supplier_id):
        BaseVO.__init__(self)
        self.operation_ukid = operation_ukid
        self.status = status
        self.ppt_relation_ukid = ppt_relation_ukid
        self.start_time = start_time
        self.end_time = end_time
        self.pass_time = pass_time
        self.service_ukid = service_ukid
        self.operation_type = operation_type
        self.supplier_id = supplier_id
