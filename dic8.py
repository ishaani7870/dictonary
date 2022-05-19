{'sonu':85,'Kartik':90,'Deepak':96,'Aman':76, 'Somesh':60,'Umesh':85,'Amarpal':70,
    'Roshan':57,
    'Riyaz':98,
    'Shabid':56}
a=int(input("enter the number"))
def my_funct():
    b=a
    i=1
    r={}
    while i<=a:
        b=i*i
        print(i,b,end="")
        n=i,b
        i=i+1
    print()
my_funct()