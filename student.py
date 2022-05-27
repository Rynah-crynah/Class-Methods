# class Student:
#     # name="Effence"
#     # age=20
#     # country="Kenya"
#     # school="AkiraChix"

from pytz import country_names


class Student:
    # school="AkiraChix" 
    def __init__(self, name,age, country, school, secondName,currentYear):
        self.name=name
        self.age=age
        self.country=country
        self.school=school
        self.secondName=secondName
        self.currentYear=currentYear


# class Student:
  
    def greeting(self):
        return f"Hello {self.name} from {self.country}, welcome to {self.school}"

    def fullName(self):
        return f'Hello {self.name} {self.secondName}'

    def year_of_birth(self):
        return f'Salma you were born in {self.currentYear-self.age}'

    def initials(self):
        return f'{self.name[0]}.{self.secondName[0]}'
    


