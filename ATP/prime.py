n=int(input('enter n: '))

for i in range(n):
          if i % 2 == 0:
            print('factors: ',i)







if n<=1:
    print('not prime')
else:
    count = 0

    for i in range(1,n+1):
           if n%i==0:
               count = count +1
          
    if count == 2:
         print('prime')

    else:
         print('not prime')
    
