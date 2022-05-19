a={'a':50, 'b':58, 'c':56,'d':40, 'e':100,'f':20}
b=[]
for i in a.keys():
    if a[i]>50:
        b.append(a[i])
print(b)
 


x=int(input("enter any num "))
y=int(input("enter any num "))
if x==1 and y==1:
  print(True)
elif x==1 and y==0:
  print(False)
elif x==0 and y==1:
  print(True)
elif x==0 and y==0:
  print(False)
else:
     print("pls enter valid number")