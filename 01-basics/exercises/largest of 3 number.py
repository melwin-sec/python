x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
z=int(input("enter 3rd number"))

if x == y == z:
    print("all 3 numbers are same and largest")
else:    
        if x == y and x > z:
           print("1st and 2nd numbers are same and largest")
        elif x == z and z > y:
           print('1st and 3rd numbers are same and largest')
        elif y == z and y > x:
           print("2nd and 3rd numbers are same and largest")
        else:
              if x > y and x > z:
                  print("1st number is largest")
              elif y > x and y > z:
                  print("2nd number is largest")
              else:
                  print("3rd number is largest")
    
