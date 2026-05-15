

class primary_tag:
    def __init__(self, name, priority, colour):
        self.__name = name
        self.__priority = priority
        self.__colour = colour

    def getName(self):
        return self.__name
    
    def getPriority(self):
        return self.__priority
    
    def getColour(self):
        return self.__colour
    
    def ToString(self):
        return self.__name + " " + str(self.__priority) + " " + self.__colour
    
    