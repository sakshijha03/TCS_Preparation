
'''
Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to cycling with his friends. 
So every time when the months starts he counts the number of sundays he will get to enjoy. Considering the month can start with any day,
be it Sunday, Monday…. Or so on. Count the number of Sunday jack will get within n number of days.
 Example 1:
Input 
mon-> input String denoting the start of the month.
13  -> input integer denoting the number of days from the start of the month.
Output :
2    -> number of days within 13 days.'''

n=int(input())
start=input().lower()
days=['mon','tue','wed','thu','fri','sat','sun']
index=days.index(start)
count=n//7
extra=n%7
if (index+extra-1)>=6:
    count+=1
print(count)