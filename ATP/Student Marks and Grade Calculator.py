print('Enter Marks of 5 Subjects')
total=0

for i in range(5):
    mark = int(input('Enter your mark: '))

    while mark < 0 or mark > 100:
       print('Invalid')
       mark =int(input("Enter mark between (0-100)"))
       


total=total+mark

print('Total Marks = ', total)
average = total / 5
print('Average Marks = ', average)
if average >= 90:
    print('Grade = A+')
elif average >= 80:
    print('Grade = A')
elif average >= 70:
    print('Grade = B')
elif average >= 60:
    print('Grade = C')
elif average >= 50:
    print('Grade = D')
else:
    print('Grade = E')
    


if mark >= 40:
    print('Result = Pass')
else:
    print('Result = Fail')
