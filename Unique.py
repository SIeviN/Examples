#!/bin/python3


#using data structures
def unique(st):
    newst = set(st)
    if len(st) != len(newst):
        print("Not unique")
    else:
        print("Unique")

#not using data structures
def unique2(st):
    for i in st:
        value = i
        index = st.index(value) + 1
        while(index < len(st)):
            if value == st[index]:
                print("Not unique")
                return False
            index += 1
    print("Unique")
    return True


print("Enter a string to check for uniqueness")
st = input()

unique(st)
unique2(st)


