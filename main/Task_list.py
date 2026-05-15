import Task
import Sub_task
import primary_tag
import Secondery_tag

class Task_list:
    def __init__(self):
        self.__tasks = []
        self.__Primary_tags = []
        self.__Secondery_tags =[]

    def addTask(self, task):
        self.__tasks.append(task)

    def getAllTasks(self):
        return self.__tasks
    
    def removeTask(self, task):
        self.__tasks.remove(task)


    def addPrimaryTag(self, tag):
        self.__Primary_tags.append(tag)

    def removeprimaryTag(self, tag):
        self.__Primary_tags.remove(tag)
    
    def getPrimaryTags(self):
        return self.__Primary_tags
    

    def addSeconderyTag(self, tag):
        self.__Secondery_tags.append(tag)

    def removeSeconderytag(self, tag):
        self.__Secondery_tags.remove(tag)

    def getSecoinderyTags(self, tag):
        return self.__Secondery_tags

