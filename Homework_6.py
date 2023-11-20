#Написати функцию, яка буде рекурсивно вираховувати число фібоначчі.

# Перший варіант
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(8))

# Другий варіант
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
print(fib(9))

# Третій варіант
def fib(n):
    if n < 2:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))
print(fib(10))
