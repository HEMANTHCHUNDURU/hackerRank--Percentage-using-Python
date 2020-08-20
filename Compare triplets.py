a=list(map(int,input().split()[:3]))
b=list(map(int,input().split()[:3]))
m=0
n=0
for i in range(0,3):
    if a[i] > b[i]:
        m=m+1
    if a[i] < b[i]:
        n=n+1
    i=i+1
print(m,n)
        
    
        

