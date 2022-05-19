from multiprocessing.sharedctypes import Value
from optparse import Values


# dict=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"}, 
#  {"six":"9"},
#  {"seven":"7"}]
# dict.Values()
# print(dict)


a=(input("enter the name"))
b=(input("enetr the name"))
if a=="true" and b=="false":
    print(f"false")
if a=="false" and b=="true":
    print(f"false")
if a=="true"and b=="true":
    print(f"true")
if a=="false" and b=="false":
    print(f"false")
