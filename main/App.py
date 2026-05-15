
import Task_list
import Task
import Sub_task
import primary_tag
import Secondery_tag


class App:
    def __init__(self):
        self.__task_list = Task_list.Task_list()
        self.populatePrimaryTags()  
        self.menu()


    def populatePrimaryTags(self):
        self.__task_list.addPrimaryTag(primary_tag.primary_tag("Important", 7, "#e37f14"))
        self.__task_list.addPrimaryTag(primary_tag.primary_tag("Verry Important", 9, "#cf1508"))
        self.__task_list.addPrimaryTag(primary_tag.primary_tag("Hobby", 3, "#1ac208"))
        self.__task_list.addPrimaryTag(primary_tag.primary_tag("normal", 5, "#f7f7f7"))

    
    def menu(self):
        choice = -2
        while  choice != -1:
            print("")
            print("")
            print("Menu:")
            print("1. display all primary tags")
            print("-1. exit")
            choice = int(input("Enter your choice: "))
            self.actions(choice)


    def actions(self, choice):
        if choice == 1:
            self.showPrimarytags()

        elif choice == -1:
            return
        

    def showPrimarytags(self):
        tags = self.__task_list.getPrimaryTags()
        print("")
        for tag in tags:
            print(tag.ToString())


    
app = App()


