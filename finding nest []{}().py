#code
st=input()
smp="([{"
f=0
pt=[]
for i in range(0,len(st)):

    if st[i] in smp:
        pt.append(st[i])
    else:
        re=pt[-1]+st[i]
        if re=="()" or re=="[]" or re=="{}":
            pt.pop()
        else:
            k=i+1 
            f=1 
            break
           
if f==1:
    print(k)
elif len(pt)==0:
    print("0")
else:
    print(str(len(st)+1))

  
print(pt)
print(len(pt))