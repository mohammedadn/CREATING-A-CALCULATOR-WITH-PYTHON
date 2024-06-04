mode = input('Enter mode you wuold like to use (+,-,*,/ )or change for cels to fh: ')
num1 = float(input("enter first number: "))
if mode == 'change':
    print(f" the temperature is {num1 * 9/5 +32} fh") 
else :
     num2 = float(input("enter second number: "))

     if mode == '+':
        print(num1 + num2)
     elif mode == '-':
        print(num1 - num2)
     elif mode == '*':
        print(num1 * num2)
     elif mode == '/':
        print(num1 / num2)  
     elif mode == 'change':
        print(f" the temperature is {num1 * 9/5 +32} fh")     
     else :
        print('Oops, try again!')    

        