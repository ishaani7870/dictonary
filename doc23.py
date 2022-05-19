from heapq import nlargest
dict = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
print("Initial Dictionary:")
print(dict, "\n")
ThreeHighest = nlargest(3,dict, key = dict.get)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for val in ThreeHighest:
    print(val, ":",dict.get(val))




 