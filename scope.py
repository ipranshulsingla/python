a=84 #global scope-> lifetime memory
def func(): 
    global a
    a=94 #local scope-> life of a  till function execution 
    b=78
    print(a)