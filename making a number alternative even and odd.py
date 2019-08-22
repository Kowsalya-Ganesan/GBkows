#code
ins=input()
print(ins)
c=0
st=""
n=1
lst=[]
vow=[]
con=[]
out=""
for i in range (0,len(ins)):
    if (ins[i].isdigit()):
       st=st+ins[i]
    elif not ins[i].isalnum():
        c+=1
n=int(st)
for i in range (0,len(st)):
    rem=int(st[i])%10

    lst.append(rem)
for i in range (0,len(lst)):
    if lst[i]%2==0:
        vow.append(lst[i])
    else:
        con.append(lst[i])
vv=len(vow)
cv=len(con)
if(c%2==0):
    if(vv==cv):
        for i in range (0,cv):
            out=out+str(vow[i])
            out=out+str(con[i])
    elif(vv>cv):
        for i in range (0,cv):
            out=out+str(vow[i])
            out=out+str(con[i])
        m=vv-cv
        for i in range (cv,vv):
            out=out+str(vow[i])
    elif(cv>vv):
        for i in range (0,vv):
            out=out+str(vow[i])
            out=out+str(con[i])
        m=cv-vv
        for i in range (vv,cv):
            out=out+str(con[i])
print(vow)
print(con)
print(out)
         
            
     
       





   


 



      


     
      




  