

class Sub_task:
    def __init__(self, title, description, end_date, start_date, completed_date):
        self.__title = title
        self.__description = description
        self.__end_date = end_date
        self.__start_date = start_date
        self.__completed_date = completed_date

    


    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description

    
    def getEndDate(self):
        return self.__end_date
    
    def getStartDate(self):
        return self.__start_date
    

    def setTitle(self, title):
        self.__title = title

    def setDescription(self, description):
        self.__description = description

    
    def setEndDate(self, end_date):
        self.__end_date = end_date

    def removeCompletedDate(self):
        self.__completed_date=None

    def setCompletedDate(self, completed_date):
        self.__completed_date = completed_date   