

# No. of test cases
t = int(input()) 

# Taking the input T times
for _ in range(t):
    
    #No. of rows and columns for the matrix
    n, m = map(int, input().split())
    
    # Taking matrix input
    matrix = [list(map(int, input().split())) for _ in range(n)]
    maxCount, rowIndex = 0, -1
    
    # Checking for no. of 1s in exery row
    for i in range(n):
        count = 0
        for j in range(m):
            if matrix[i][j] == 1:
                count += 1
        
        if count > maxCount:
            maxCount = count
            rowIndex = i
    print(rowIndex)
    
    
