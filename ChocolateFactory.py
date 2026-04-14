'''
 *  A chocolate factory is packing chocolates into the packets. The chocolate packets here 
 * represent an array of N number of integer values. The task is to find the empty packets(0) of 
 * chocolate and push it to the end of the conveyor belt(array). Click here to see solution
Example 1 : N=8 and arr = [4,5,0,1,9,0,5,0].

There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array
 '''
 
def move_Zero(arr):
    pos=0
    for num in range (len(arr)):
        if arr[num] !=0:
            arr[num],arr[pos]=arr[pos],arr[num]
            pos+=1
    return arr
n=int(input())
arr=list(map(int,input().split(',')))
result=(move_Zero(arr))
print(result)


'''if want to count the numebr of empty packet then do this 

n=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    if i ==0:
        count+=1
print(count)

'''