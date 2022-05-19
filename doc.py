d={1:100,2:100,3:300,4:100}
d1={}
for i,j in d.items():
    if j not in d1.values():
        d1[i]=j
print(d1)