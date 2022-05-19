dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}

a={}
for i in dic1:
    for k in dic2:
        for l in dic3:
            if i==k:
                m=(dic1[i]+dic2[k])
a.update({1:10,2:20})
a.update({3:30,2:40})
a.update({k:m})
a.update({3:30})
a.update({5:50})
a.update({6:60})
print(a)