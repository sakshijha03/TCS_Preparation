'''  
Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.
Note : 1st element of the array should be considered in the count of the result.
For example,
Arr[]={7,4,8,2,9}
As 7 is the first element, it will consider in the result.
8 and 9 are also the elements that are greater than all of its previous elements.
Since total of  3 elements is present in the array that meets the condition.
Hence the output = 3.
'''
n=int(input())
arr=list(map(int,input().split())) 
count=1
max_so_far=arr[0]
for i in range (1,len(arr)):
   
    if arr[i]>max_so_far:
        count+=1
        max_so_far=arr[i]
print(count)