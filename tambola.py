import time
numbers=[]
for i in range(1,101):
    no={"Number":i,"isMarked":False}
    numbers.append(no);
print(numbers)
time.sleep(5)
numbers[99]["isMarked"]=True
print(numbers)
