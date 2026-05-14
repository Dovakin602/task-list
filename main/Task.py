

class Task:
    def __init__(self, title, description, primary_tag, secondery_tags, end_date, start_date, completed_date, sub_tasks):
        self.title = title
        self.description = description
        self.primary_tag= primary_tag
        self.secondery_tags = secondery_tags
        self.end_date = end_date
        self.start_date = start_date
        self.completed_date = completed_date
        self.sub_tasks = sub_tasks

    


    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description

    def getPrimaryTag(self):
        return self.primary_tag
    
    def getSeconderyTags(self):
        return self.secondery_tags
    
    def getEndDate(self):
        return self.end_date
    
    def getStartDate(self):
        return self.start_date
    
    def getSubTasks(self):
        return self.sub_tasks
    

    def setTitle(self, title):
        self.title =title

    def setDescription(self, description):
        self.description = description

    def addSeconderyTag(self, secondery_tag):
        for i in self.secondery_tags:
            if secondery_tag == i:
                return False
        self.secondery_tags.append(secondery_tag)
        return True

    def removeSeconderyTag(self, secondery_tag):
        for i in self.secondery_tags:
            if secondery_tag == i:
                self.secondery_tags.remove(i)
                return True
        
        return False
        
    
    def setEndDate(self, end_date):
        self.end_date = end_date

    def removeCompletedDate(self):
        self.completed_date=None

    def setCompletedDate(self, completed_date):
        self.completed_date = completed_date   

    def addSubTask(self, sub_task):
        for i in self.sub_tasks:
            if sub_task == i:
                return False
        self.sub.append(sub_task)
        return True
    
    def removeSubTask(self, sub_task):
        for i in self.sub_tasks:
            if sub_task == i:
                self.sub_tasks.remove(i)
                return True
        
        return False




    
   