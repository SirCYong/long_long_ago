from .BaseVO import BaseVO


class CmParticipant(BaseVO):

    def __init__(self, participant_ukid, ppt_name, ppt_relation_ukid, ppt_type, identify_id):
        BaseVO.__init__(self)
        self.participant_ukid = participant_ukid
        self.ppt_name = ppt_name
        self.ppt_relation_ukid = ppt_relation_ukid
        self.ppt_type = ppt_type
        self.identify_id = identify_id

