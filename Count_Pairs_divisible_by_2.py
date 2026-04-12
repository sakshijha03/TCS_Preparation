
# t is the no. of test cases
t = int(input())
while t > 0:
    N=int(input())
    L=list(map(int,input().split()))
    oc=0
    ec=0
    for i in L:
        if i%2 ==0:
            ec+=1
        else:
            oc+=1
    a=(ec*(ec-1)//2)+(oc*(oc-1)//2)
    print(a)
    t -= 1
