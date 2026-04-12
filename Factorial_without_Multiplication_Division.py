# Function for checking the Factorial

def factorial(n):
    fact = 1
    
    # calculating the factorial
    for i in range(2, n + 1):
        temp = 0
        
        # adding the fact i times
        for j in range(i):
            temp += fact
        fact = temp
    return fact


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(factorial(n))


if __name__ == "__main__":
    main()