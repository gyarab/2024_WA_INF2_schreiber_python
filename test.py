def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer") or n < 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def is_prime(number) -> bool:
    if not isinstance(number, int) or number =< 0:
        raise ValueError("number must be a non-negative integer")
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(fibonacci(10)) 
    print(is_prime(10))
