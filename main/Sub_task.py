

class Sub_task:
    def __init__(self, title, description, end_date, start_date, completed_date):
        self.title = title
        self.description = description
        self.end_date = end_date
        self.start_date = start_date
        self.completed_date = completed_date

    


    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description

    
    def getEndDate(self):
        return self.end_date
    
    def getStartDate(self):
        return self.start_date
    

    def setTitle(self, title):
        self.title =title

    def setDescription(self, description):
        self.description = description

    
    def setEndDate(self, end_date):
        self.end_date = end_date

    def removeCompletedDate(self):
        self.completed_date=None

    def setCompletedDate(self, completed_date):
        self.completed_date = completed_date   