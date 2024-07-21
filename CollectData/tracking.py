class visitors():
    def __init__(self, datum):
        self.datum = datum
    def visitDatum(self):
        return 'visit'
    def markDataToTrack(self):    
        None