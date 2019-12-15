a=input()
l=len(a)
x=1
y=l
print(a)
for i in range(len(a)):
    print(a[0:l-1]+("*"*x))
    print(("*"*x)+a[x:y+1])
    x+=1
    l-=1
