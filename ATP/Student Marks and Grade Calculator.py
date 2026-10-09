print('Enter Marks of 5 Subjects')
sub1 = int(input('Enter mark of subject 1: '))
sub2 = int(input('Enter mark of subject 2: '))
sub3 = int(input('Enter mark of subject 3: '))
sub4 = int(input('Enter mark of subject 4: '))
sub5 = int(input('Enter mark of subject 5: '))
total = sub1 + sub2 + sub3 + sub4 + sub5
print('Total Marks = ', total)
Average = total / 5
print('Average Marks = ', Average)
if Average >= 90:
    print('Grade = A+')
elif Average >= 80:
    print('Grade = B')
elif Average >= 70:
    print('Grade = C')
elif Average >= 60:
    print('Grade = D')
elif Average >= 50:
    print('Grade = E')
elif Average >= 40:
    print('Grade = F')
else:
    print('Grade = E')


if Average >= 40:
    print('Result = Pass')
else:
    print('Result = Fail')
