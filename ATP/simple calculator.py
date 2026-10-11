a=int(input('enter a'))
b=int(input('enter a'))
op=input('enter op')

match op:
    case '+':
        c=a+b
    case '-':
        c=a-b
    case'*':
        c=a*b
    case '/':
        if b!=0:
            c=a/b
        else:
            c='enter other than 0'
    case _:
       c = 'invalid'

print(c)

