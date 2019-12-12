def duplicates(x):
    s=""
    x.lower()
    for i in x:
        if(i not in s):
            s+=i
    return s
a=input()
print(a)
a=duplicates(a)
print(a)
