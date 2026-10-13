
n = int(input('Enter n: '))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n and n > 0:
    print('perfect number')
else:
    print('not a perfect number')
