# Write generator, which generates numbers in a given range (from a certain number to a certain number)

def gen():
    for numbers in range(17, 6, -1):
        yield numbers

for numbers in gen():
    print(numbers)
