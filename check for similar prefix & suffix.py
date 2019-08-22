#code
st=input()
l=len(st)
pt=st[::-1]
c=0
for i in range(0,len(st)):
    if st[i]!=pt[i]:
        c=i
        break
if(c==0):
    print("-1")
elif(c>0):
    print(c)

    
      
input:
    xxabcxxabcxx 
output:
    2
