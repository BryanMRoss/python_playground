def wind_speed(windnum):
    num = int(windnum)
    wlevel = 0
    if num > 73 and num < 96:
        wlevel = 1
    elif num > 95 and num < 111:
        wlevel = 2
    elif num > 110 and num < 131:
        wlevel = 3
    print("the storm wind level =", wlevel)

wind_number = input ("Enter a wind speed: ")
wind_speed(wind_number)

#FOR FUN (playing with dictionaries,lists, sets)
# purpose is to compile lists of keys for common values,
# so you end up with two keys listed in the randy list and one in
# the bob list
# should return {'randy':['key1', 'key3'], 'bob': ['key2']}
filedict = {"key1": "randy", "key2": "bob", "key3":"randy"}
unique_values = set(filedict.values())
list_of_lists = {} # initialize a dictionary
for uval in unique_values:
    mylist = []
    for k in filedict:
        if filedict[k] == uval:
            mylist.append(k)
    list_of_lists[uval] = mylist
print(list_of_lists)
            


        
