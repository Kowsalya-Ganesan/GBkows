import sys

if __name__ == '__main__':
    st=raw_input()
    lst=[]
    ma=0
    for i in st:
        if i.isdigit():
            lst.append(i)
    print(lst)
    s=str(lst)
    for i in lst:
        c=lst.count(i)
        if c>ma:
            ma=c
            k=i
    print k
            
        
        
     

