"""
while(condition):
    statements...
    statements...

for <control_variable> in <collection/sequence>:
    statements...
    statements...
"""
while(True):
    print("1. Addition")
    print("2. Subtract")
    print("0 Exit")
    choice=input("Select:")
    if(choice=="1"):
        num1=int(input("Enter num 1:"))
        num2=int(input("Enter num 2:"))
        res=num1+num2
        print("Result is",res)
    elif(choice=="2"):
        num1=int(input("Enter num 1:"))
        num2=int(input("Enter num 2:"))
        res=num1-num2
        print("Result is",res)
    elif(choice=="0"):
        exit()
    else:
        print("Invalid Choice")