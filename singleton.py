class Singleton:
        __instance = None
        @staticmethod
        def getInstance():
            if Singleton.__instance == None:
                Singleton()
            return Singleton.__instance

        def __init__(self):
            if Singleton.__instance!= None:
                raise Exception("this class is a singleton")
            else:
                Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.getInstance()
print(s) 


##A Singleton candidate must satisfy three requirements:

##controls concurrent access to a shared resource.
##access to the resource will be requested from multiple, disparate parts of the system.
##there can be only one object.