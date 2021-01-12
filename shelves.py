# dictionaries
import shelve
class dictionary_maker:  
    def __init__(self):
        self.test_shelve = shelve.open('student_scores.txt', 'c')
        self.keys_numbers = {'fish':1, 'golf':3, 'sky':1, 'pen':2}

    def hello(self):
        return 'HELLO'

    def record_grades(self):
        name = str(input ('Enter student name: '))
        grade = str(input('Enter grade for ' + str(name) + ':(-999 to quit) '))
        while grade != '-999':
            self.test_shelve[name] = grade
            # let's get another name and grade, unless I want to quit (-999)
            name = str(input ('Enter student name: '))
            grade = str(input('Enter grade for ' + str(name) +
                               ': (-999 to quit) '))

    def get_grade(self, student_name):
        return_val = self.test_shelve.get(student_name, student_name
                                        + ' NOT FOUND')
        self.test_shelve.close()
        return return_val
    
    
my_dm = dictionary_maker()
print(my_dm.hello())
my_dm.record_grades()
print( 'The grade for Skippy is', my_dm.get_grade('Skippy'))
