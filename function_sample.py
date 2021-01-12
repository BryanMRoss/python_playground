# Function example in a loop. This will print a table of celcius temps between
# 0 and 100 in increments of 10
def convert_to_fahrenheit(celcius):
    """this converts the celcius number to fahrenheit"""
    f = 9.0/5.0 * celcius + 32
    return f

for celcius in range(0, 101, 10):
    print("Celcius value", celcius, "\t", "=", "\t", convert_to_fahrenheit(celcius))

