#code
n=[]
ls=int(input())

for i in range (0,ls):
    
    el=int(input())
    n.append(el)
print(n)
l=len(n)
print(l)
for i in range (0,l):
    n[i]=int(n[i])
    t=n[i]
    c=0
    sum=0
    while(n[i]!=0):
        r=n[i]%10
        sum=sum+r
        n[i]=n[i]//10

    print(sum)
    if(t%sum==0):
        print("yes")
    else:
        print("no")

 
 
 
