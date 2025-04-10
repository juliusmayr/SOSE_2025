from my_functions import estimate_max_hr
from my_functions import calculate_age
from my_functions import estimate_max_hr 


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    def __init__(self, first_name, last, sex, age):
        super().__init__(first_name, last)
        self.sex = sex  
        self.__birthdate = datetime.strptime(age, "%Y-%m-%d").date()
    
    def __calculate_age(self):
        today = date.today()
        return today.year - self.__birthdate.year - ((today.month, today.day) < (self.__birthdate.month, self.__birthdate.day))

    def estimate_max_hr(self, sex, age):
      age = self.__calculate_age()
      return estimate_max_hr(age, self.sex)

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