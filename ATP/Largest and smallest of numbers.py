n = int(input('How many numbers? '))

num = int(input('Enter first number: '))

largest = num
smallest = num

for i in range(n-1):
    num = int(input('Enter number: '))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print('Largest =', largest)
print('Smallest =', smallest)
