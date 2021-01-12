# lists and tuples
# note that lists are completely mutable and unrestricted
# tuples are immutable and preferred for efficiency as well as arguments
# and return values for a lot of functions
class Average_it():
    def __init__(self):
        self.number_list = []
        self.sum = 0.0
    def avg_numbers(self):
        self.user_number = eval(input("Enter a number. -999 will exit: "))
        while self.user_number != -999:
            self.number_list.append(self.user_number)
            self.sum = self.sum + self.user_number
            print(self.number_list)
            print("Average =", self.sum / len(self.number_list))
            self.user_number = eval(input("Enter a number. -999 will exit: "))

test_averages = Average_it()
test_averages.avg_numbers()
# example of a tuple
thisTuple = ('apple', 'banana', 'cherry')
print (thisTuple)

# extra information for Python sorting:
# http://wiki.python.org/moin/HowTo/Sorting
        
