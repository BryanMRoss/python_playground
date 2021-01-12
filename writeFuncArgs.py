def write_backwards(*args):
    i = len(args) - 1
    if i < 0:
        print ("No arguments")
    while (i + 1) > 0:
        print (args[i])
        i = i - 1
    return

def write_forwards(*args):
    i = len(args)
    if i < 1:
        print ("No arguments.")
    else:
        for x in range(i):
            print (args[x])
    return


print ("first with no arguments...")
write_backwards()
print ("now with three arguments...")
write_backwards("22", "33", "44")
print ("now write forwards with no arguments...")
write_forwards()
print ("now with three arguments...")
write_forwards("22", "33", "44")
