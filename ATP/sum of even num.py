
n = int(input('Enter n: '))
sum = 0

for i in range(1, n + 1):
    num = int(input('Enter number: '))

    if num % 2 == 0:
        sum = sum + num

print('sum of even numbers:', sum)
