from .BaseVO import BaseVO


class OrderTask(BaseVO):

    def __init__(self, operation_ukid, start_time, operation_task_ukid, object_type,
                 operation_object, ukid,
                 ppt_relation_ukid, ppt_name, server_time):
        BaseVO.__init__(self)
        self.operation_ukid = operation_ukid
        self.start_time = start_time
        self.operation_task_ukid = operation_task_ukid
        self.object_type = object_type
        self.operation_object = operation_object
        self.ukid = ukid
        self.ppt_relation_ukid = ppt_relation_ukid
        self.ppt_name = ppt_name
        self.server_time = server_time

