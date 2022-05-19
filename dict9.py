{'M':1,'I':4,'S':4,'P':2}
a="MISSISSIPPI"
b={}
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c=c+1
        b.update({a[i]:c})
        c=c+1
print(b)
    