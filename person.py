'''

Sirajuddin Sayed, M00850971, Miniproject, SOB:32,33,34,35

This program that uses classes and attributes to display student details.
There is super class named 'person' which has a sub-class of student
named, 'student'
'''
class person():
    def __init__(self,roll_number,first_name,last_name,date_of_birth,gender,nationality,profession,year_of_study,faculty,tuition_fees):
        self.roll_number= roll_number
        self.first_name= first_name
        self.last_name=  last_name
        self.date_of_birth= date_of_birth
        self.gender= gender
        self.nationality= nationality
        self.profession= profession
        self.year_of_study= year_of_study
        self.faculty= faculty
        self.tuition_fees= tuition_fees
        
#created attributes for the person 'student'

    def __str__(self):
        return f'{self.first_name}{self.last_name}\n'
    
#returns the following as a string 'first_name' and 'last_name' as an introductory before displaying all the details

class student(person):
    def __init__(self,roll_number,first_name,last_name,date_of_birth,gender,nationality,profession,year_of_study,faculty,tuition_fees):
        super().__init__(roll_number,first_name,last_name,date_of_birth,gender,nationality,profession,year_of_study,faculty,tuition_fees)

#created a sub-class 'student' inherited from 'person'
        
    def __str__(self):
        return super().__str__() + f' MISIS: {self.roll_number},\n '\
            f'first name: {str(self.first_name)},\n '\
            f'last name: {str(self.last_name)},\n '\
            f'date_of_birth: {self.date_of_birth},\n '\
            f'gender: {str(self.gender)}, \n '\
            f'nationality: {str(self.nationality)}, \n '\
            f'profession: {str(self.profession)}, \n '\
            f'year of study: {str(self.year_of_study)}, \n'\
            f' faculty: {str(self.faculty)},\n'\
            f' tuition_fees: {self.tuition_fees} AED \n'\

#made a display format for atrributes to be presented when printed









