# test the time class
from time_class import Time

my_time = Time()

my_time.print_time()
my_time.set_time(4, 30, 54)
my_time.print_time()
print(my_time.get_time())
print("My hours =", my_time.get_time()["H"])

for i in range(130):
    my_time.tick()
    print(my_time.get_time())




