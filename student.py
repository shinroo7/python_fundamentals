#class: create a new data type 
#use with class.py

class Student:

    def __init__(self, name, major, gpa, is_on_probation): #pass the values to the real objects
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        