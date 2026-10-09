usernames = ['admin', 'melwin', 'pranav', 'sanju', 'rayan', 'sanjay']
passwords = ['admin@123', 'melwin@123', 'pranav@123', 'sanju@123', 'rayan@123', 'sanjay@123']

user_entered_username = input('Enter your username: ')
user_entered_password = input('Enter your password: ')

for i in range(len(usernames)):
    if usernames[i] == user_entered_username:
        if passwords[i] == user_entered_password:
            print('Login successful')
        else:
            print('Login failed! Invalid password')
        break
else:
    print('Login failed! Invalid username')
