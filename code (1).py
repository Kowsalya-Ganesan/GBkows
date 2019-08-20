#code
n=input()
lst=[]
for i in range(0,len(n)):
    if i%2==0:
        k=int(n[i])+1
        lst.append(k)
    else:
        k=int(n[i])-1
        lst.append(k)
for i in range (0,len(lst)):
    print(lst[i],end=" ")
        
     
