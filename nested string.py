s=input()
p=[]
f=0
smp="([{"
tot="(){}[]"
for i in range (0,len(s)):
    if s[i] in smp:
        p+=[s[i]]
    else:
        r=p[-1]+s[i] 
        if r=="()" or r=="[]" or r=="{}":
            p.pop()
        else:
            k=i+1
            f=1
            break
if(f==1):
    print(k)
elif(len(p)==0):
    print("0")
else:
    print(str(len(s)+1))
    
  
input:               output:

    {([])}[]             0
    ([)()]               3
    [[()]                6
  
    
