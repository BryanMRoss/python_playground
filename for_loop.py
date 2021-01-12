# prompt user for numbers and add them up. When the user says
# -1, then you break the loop and report sum and average
sumit = 0.0
num_numbers = 0
average = 0
while True:
        ns = eval(input("Enter a number (-1 exits): "))
        if ns < 0.0:
                break
        sumit = sumit+ns
        num_numbers = num_numbers + 1
print("SUM = ", sumit)
if num_numbers != 0:
        average = sumit/num_numbers
print("AVG = ", average)


# another way that doesn't need a break
print("ANOTHER WAY...")
sumit = 0.0
num_numbers = 0
average = 0
ns = eval(input("Enter a number (-1 exits): "))
while ns != -1:
        sumit = sumit+ns
        num_numbers = num_numbers + 1
        ns = eval(input("Enter a number (-1 exits): "))
print("SUM = ", sumit)
if num_numbers != 0:
        average = sumit/num_numbers
print("AVG = ", average)
