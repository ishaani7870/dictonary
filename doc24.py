from collections import defaultdict
l=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
{'item': 'item1', 'amount': 750}]
d=defaultdict(int)
for i in l:
    d[i['item']] += i['amount']
print(d)


# x = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result={}
# for d in x:
#     if d['item'] in result:
#         result[d['item']] += d['amount']
# else:
#     result[d['item']] = d['amount']

# print(result)


