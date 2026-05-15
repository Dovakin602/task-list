

class Task:
    def __init__(self, title, description, primary_tag, secondery_tags, end_date, start_date, completed_date, sub_tasks):
        self.__title = title
        self.__description = description
        self.__primary_tag= primary_tag
        self.__secondery_tags = secondery_tags
        self.__end_date = end_date
        self.__start_date = start_date
        self.__completed_date = completed_date
        self.__sub_tasks = sub_tasks

    


    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description

    def getPrimaryTag(self):
        return self.__primary_tag
    
    def getSeconderyTags(self):
        return self.__secondery_tags
    
    def getEndDate(self):
        return self.__end_date
    
    def getStartDate(self):
        return self.__start_date
    
    def getSubTasks(self):
        return self.__sub_tasks
    
    def getPriority(self):
        return self.__primary_tag.getPriority()
    

    def setTitle(self, title):
        self.__title = title

    def setDescription(self, description):
        self.__description = description

    def addSeconderyTag(self, secondery_tag):
        for i in self.__secondery_tags:
            if secondery_tag == i:
                return False
        self.__secondery_tags.append(secondery_tag)
        return True

    def removeSeconderyTag(self, secondery_tag):
        for i in self.__secondery_tags:
            if secondery_tag == i:
                self.__secondery_tags.remove(i)
                return True
        
        return False
        
    
    def setEndDate(self, end_date):
        self.__end_date = end_date

    def removeCompletedDate(self):
        self.__completed_date=None

    def setCompletedDate(self, completed_date):
        self.__completed_date = completed_date   

    def addSubTask(self, sub_task):
        for i in self.__sub_tasks:
            if sub_task == i:
                return False
        self.__sub.append(sub_task)
        return True
    
    def removeSubTask(self, sub_task):
        for i in self.__sub_tasks:
            if sub_task == i:
                self.__sub_tasks.remove(i)
                return True
        
        return False




    
   