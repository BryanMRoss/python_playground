# Exceptions assignment

counter = 1
try:
    while (counter >= 1):
        number = 2.0 ** counter
        counter = counter + 0.001
except OverflowError as ofe:
    print ("Whoops! OverflowError")
except KeyboardInterrupt as kbi:
    print ("Whoops! KeyboardInterrupt")
finally:
    print ("My number go up to", number)
