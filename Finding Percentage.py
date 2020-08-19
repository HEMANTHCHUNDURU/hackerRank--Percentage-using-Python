n=int(input())
c=0
a={}
for i in range(0,n):
    name,x,y,z=input().split()
    w=float(x)
    e=float(y)
    r=float(z)
    score=float((w+e+r)/3)
    a[name] = score
m=input()
j=a[m]
print("{:.2f}".format(j))
