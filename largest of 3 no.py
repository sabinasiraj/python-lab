num1=float(input("enter first number:"))
num2=float(input("enter 2nd number:"))
num3=float(input("enter 3rd number:"))
if(num1>=num2) and (num1>=num3):
    max=num1
elif(num2>=num1) and (num2>=num3):
    max=num2
else:
     max=num3
print("largest number is",max)
        
    


