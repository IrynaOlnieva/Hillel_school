def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(start, end):
    for num in range(start, end + 1):
        if prime(num):
            yield num

start = 20
end = 70

print(f"Found prime numbers from the range {start}:{end}")
for num in prime_numbers(start, end):
    print(num, end=", ")
