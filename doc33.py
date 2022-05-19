dict1 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
dict2 = dict(sorted(dict1.items(),key = lambda e: e[1])[-3:])
for k,v in dict2.items():
    print(k,v)