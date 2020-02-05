a=int(input())
l=[]
j=1
x = str(a)*(2**(a-1))
x1=len(x)
l.append(x)
for i in range(a-1,0,-1):
    x = str(i)*(2**(i-1))
    y = str(j)*(x1-len(x))
    x1=len(x)
    l.append(x+y)
    j+=1
for i in l:
    if(len(i)==(2**(a-1))):
        print(i)
    else:
        x=(2**(a-1))//len(i)
        i=i*x
        print(i)
