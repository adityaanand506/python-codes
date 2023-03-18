#check prime in a range
l,r =map(int,input().split())
prime=[1]*(r+1)
prime[1]=0
for i in range(2,int(r**.5)+1):
    if prime[i]:
        for j in range(i*2,r+1,i):
            prime[j]=0
for i in range(l,r+1):
    if prime[i]:print(i,end=" ")
