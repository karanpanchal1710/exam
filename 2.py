try:
    print("try block")
    num1=int(input("Enter first number"))
    num2=int(input("Enter another number"))
    res=num1/num2
except:
    print("Except block")
    print("Number1 is not divisible by zero")
else:
    print("Else block") 
    print("Output  ",res)
finally:
    print("Exceptional handling program")   