def sum_of_occurrences(str1, str2):
    summ = 0
    freq_map = set(str2)
    for i in range(len(str1)):
        if str1[i] in freq_map:
            summ+=1
    return summ
T = int(input())
for _ in range(T):
    str1 = input().strip()
    str2 = input().strip()
    print(sum_of_occurrences(str1, str2))