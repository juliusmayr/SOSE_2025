from my_functions import estimate_max_hr

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    def __init__(self, first_name, last, sex, age):
        super().__init__(first_name, last)
        self.sex = sex  
        self.__age = age 

    def estimate_max_hr(self, sex, age):
      """A function that estimates the maximum heart rate of a subject"""
      return estimate_max_hr(sex, age)

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

class Experiment():
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor