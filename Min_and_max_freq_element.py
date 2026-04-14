arr=list(map(int,input().split()))
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
min_ele= min(freq,key=freq.get)
max_ele= max(freq,key=freq.get)
print(min_ele,max_ele)