st=input()
p=st.split(",")
q=[]
for i in p:
    q.append(i.split(":"))
for i in range (len(q)):
    f=q[i]
   
arr1=sorted(q,key=lambda x:x[1])

arr2=sorted(q,key=lambda x:x[2])
arr2.reverse()
print (arr1)
print (arr2)
z=[]
for i in range(len(q)):
    if (arr1[i]==arr2[i]):
        z.append(arr1[i])
if(len(z)==0):
    print("x")
elif(len(z)==1):
    print(z[0][0])
else:
    for i in range(0,len(z)-1):
       n=z[i]
       print(n[0],end=":")
       p=z[len(z)-1]
       print(p[0])
      
        



