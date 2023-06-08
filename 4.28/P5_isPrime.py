n = int(input())
prime_and_3k_1 = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def create_prime_list(n):
    prime_list = []
    for num in range(2, n+1):
        if is_prime(num) and (num % 3 == 2):
            prime_and_3k_1.append(num)
    return prime_and_3k_1

create_prime_list(n)

print(prime_and_3k_1)