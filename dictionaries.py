# dictionaries
class dictionary_maker:
    def __init__(self):
        self.test_dictionary = {}
        self.keys_numbers = {'fish':1, 'golf':3, 'sky':1, 'pen':2}

    def hello(self):
        return 'HELLO'

    def record_grades(self):
        name = str(input ('Enter student name: '))
        grade = str(input('Enter grade for ' + str(name) + ':(-999 to quit) '))
        while grade != '-999':
            self.test_dictionary[name] = grade
            # let's get another name and grade, unless I want to quit (-999)
            name = str(input ('Enter student name: '))
            grade = str(input('Enter grade for ' + str(name) +
                               ': (-999 to quit) '))
    def get_sample_dictionary(self):
        return self.keys_numbers
    

    def get_grade(self, student_name):
        return self.test_dictionary.get(student_name, student_name
                                        + ' NOT FOUND')
    
my_dm = dictionary_maker()
print('test dictionary display...')
print(my_dm.get_sample_dictionary())
for dkey in my_dm.get_sample_dictionary().keys():
    print ("key = " + dkey + " value =", my_dm.get_sample_dictionary().
           get(dkey))

print(my_dm.hello())
my_dm.record_grades()
print( 'The grade for Skippy is', my_dm.get_grade('Skippy'))
