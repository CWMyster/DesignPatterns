from model import Person

def showAllView(list):
    print (len(list))
    for item in list:
        print (item.name())

def startView():
    print('MVC - the simplest example')
    print('Do you want to see everyone in db?')

def endView():
    print('Goodbye')
