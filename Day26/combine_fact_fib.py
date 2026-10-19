def factorial(n):
    return 1 if n<= 1 else n * factorial(n - 1)

def fibonacci(n, dp={0:0, 1:1}):
    if n not in dp:
        dp[n] = fibonacci(n - 1, dp) + fibonacci(n - 2, dp)
    return dp[n]

if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci 10:",fibonacci(10))
