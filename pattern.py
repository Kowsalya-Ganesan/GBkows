#code

val=1
n=int(input())
c=int(input())
v=2*c
for i in range (0,n):
    if(i%2==0):
        for j in range (0,c):
            print(val,end=" ")
            val=val+1
        val=val+c
        print("\n")
    else:
        for j in range (0,c):
            print(v,end=" ")
            v=v-1 
        v=(v+1)+((2*c)+(c-1))
        print("\n")
