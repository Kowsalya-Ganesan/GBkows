#code
n=int(input())
lst=[]
ne=[]
for i in range(0,n):
    d=input().split()
    lst.append(d)
    k=lst[i]
    avg=sum(map(float,k[1:]))/3
    ne.append(avg)
print(ne)
t=max(ne)
print(t)
for i in range (0,len(ne)):
    if(ne[i]==t):
        ind=i
print(ind)
print(lst[ind][0])







   

