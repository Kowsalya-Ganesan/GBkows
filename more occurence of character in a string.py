#code
st=input()
lst=[]
for i in range (0,len(st)):
    if(st[i].isalpha()):
        lst.append(st[i])
for i in range (0,len(lst)):
    for j in range (i+1,len(st)):
        if(st[i]==st[j]):
            print(st[i])
         
         

  
