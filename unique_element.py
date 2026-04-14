arr=list(map(int,input().split(",")))
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
for key in freq:
    if freq[key] ==1:
        print(key)