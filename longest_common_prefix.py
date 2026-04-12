def common_prefix(strs):
    if not strs:
        return -1
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == '':
                return -1
    return prefix

T = int(input())
for _ in range(T):
    N = int(input())
    strs = input().split()
    print(common_prefix(strs))