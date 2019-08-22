#code
st=input()
pt=st.split (",")
print(pt)
al=[]
nl=[]
fa=[]
fn=[]
h=[]
for i in range(0,len(pt)):
   h=pt[i]
   for j in range(len(h)):
        if h[j].isalpha():
           al.append(h[j])
        else:
            nl.append(h[j])
  
c=0
m=0
print(al,nl)  
for i in range (len(al)):
    for j in range (i+1,len(al)):
        if(al[i]==al[j]):
            c=c+1 
            if(c>=2):
                a=al[i]
for i in range(len(pt)):
    if a in pt[i]:
        fa.append(pt[i])
print(c)
for i in range(len(nl)):
    for j in range(i+1,len(nl)):
        if (nl[i]==nl[j]):
            m=m+1 
            if m>=2:
                n=nl[i]
for i in range(len(pt)):
    if n in pt[i]:
        fn.append(pt[i])
print(m)
if m>=2 and c>=2:
    print(fn)
    print(fa)
elif m>=2:
    print(fn)
elif c>=2:
    print(fa)
else:
    print("-1")


  
     
        



    

    

  




     

      

