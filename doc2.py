a='w3resource'
b={}
for i in range (len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c=c+1
            b.update({a[i]:c})
print(b)