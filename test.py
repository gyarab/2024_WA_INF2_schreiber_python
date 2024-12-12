def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer") or n < 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__":
    print(fibonacci(10))
