class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

student1 = Student()


student1.setName("Karthik")
student1.setRollNumber(35)


print(student1.getName()) 
print(student1.getRollNumber())