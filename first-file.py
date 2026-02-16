a=int(input())
b=int(input())
for i in range(a,b+1):
    n=False
    for j in range(2,i):
        if i%j==0:
            n=True
            break
    if n==False and i>1:
        print(i)