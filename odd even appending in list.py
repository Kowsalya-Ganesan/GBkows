#code
n=int(input())
lst=[]
odd=[]
eve=[]
out=[]
for i in range(0,n):
    e=input()
    lst.append(e)
l=len(lst)
for i in range (0,l):
    if(int(lst[i])%2==0):
        odd.append(lst[i])
    else:
        eve.append(lst[i])
oc=len(odd)
ec=len(eve)
if(oc==ec):
    lst.reverse()
    for i in range (0,len(lst)):
        out.append(lst[i])
elif(oc>ec):
    odd.reverse()
    for i in range (0,oc):
        out.append(odd[i])
    for i in range(0,ec):
        out.append(eve[i])
elif(ec>oc):
    eve.reverse()
    for i in range (0,ec):
        out.append(eve[i])
    for i in range (0,oc):
        out.append(odd[i])
print(out)
    
    

