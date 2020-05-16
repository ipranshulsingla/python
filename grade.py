"""
*
* *
* * *
* * * *
* * * * *
"""
marks=int(input("Enter your marks:"))
grade=""
# 100>=marks>=90
if(marks<=100 and marks>=90):
    grade="A"
elif(marks<90 and marks>=75):
    grade="B"
elif(marks<75 and marks>=60):
    grade="C"
elif(marks<60 and marks>=40):
    grade="D"
elif(marks<40 and marks>=33):
    grade="E"
else:
    if(marks>=0 and marks<=100):
        grade="F"
    else:
        grade="Invalid Grade"
print('Your Marks:',marks)
print('Your Grade:',grade)