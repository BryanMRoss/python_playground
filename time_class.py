# python class file for making a Time class.
class Time:
    """This is a class to report hours, minutes, and seconds"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        # the dunder before the name is convention to encourage using
        # getters & setter instead of assigning directly. If you were
        # to try to reference direction, like my_time_object.__hour, you would
        # get an error. You would have to say my_time_object._Time__hour insead.
        
    def print_time(self):
        """print out the time"""
        print(self.__hour, ":", self.__minute, ":", self.__second)

    def set_time(self, hour, minute, second):
        """set the time"""
        if hour >= 0 and hour <= 24:
            self.__hour = hour
        else:
            print("hour must be 0 to 24 range")

        if minute >= 0 and minute <= 60:
            self.__minute = minute
        else:
            print("minute must be 0 to 60 range")

        if second >= 0 and second <= 60:
            self.__second = second
        else:
            print("second must be 0 to 60 range")
        

    def get_time(self):
        """return a dictionary of the time in H, S, M keys"""
        time_dictionary = {
            "H": self.__hour,
            "M": self.__minute,
            "S": self.__second
            }
        return time_dictionary

    def tick(self):
        """This adds another second to the time"""
        # tick off another second and check to see if it crosses 60
        # to change the minutes and if minutes updates hours

        # if current seconds is 59, then update the minute
        if self.__second == 59:
            self.__second = 0
            # update the minute
            if self.__minute == 59:
                self.__minute = 0
                # update the hour
                if self.__hour == 24:
                    self.__hour = 1
                else:
                    self.__hour = self.__hour + 1
            else:
                self.__minute = self.__minute + 1
        else:
            self.__second = self.__second + 1
        return None

 
myWatch = Time()
myWatch.set_time(11, 35, 59)
print (myWatch.get_time())
myWatch.tick()
print (myWatch.get_time())
print ("EXAMPLE OF HOW TO FORCE AROUND NAME MANGLING")
# example of name mangling. Note that a dunder-NAME object gets "mangled",
# i.e., it gets pre-pended with _[CLASS NAME] so it can't be referred to
# directly outside the class (unless you want to, as in the example)
class Myclass:
    def __init__(self, animal):
        self.creature = str (animal)
        self.__aussy = "kangaroo"  # should provide a getter/setter if needed

    def show_animal(self):
        print (self.creature)

nature = Myclass("Lion")
nature.show_animal()
print (dir (nature))
print (nature._Myclass__aussy)
