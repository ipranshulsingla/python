"""
Row=4
1st row= 1
2nd row=2
3rd row=3
*
* *
* * *
* * * *
"""


rows=int(input("Enter rows:")) #5
for row in range(1,rows+1): #1X,2X,3X,4,5 -> row 3
    for col in range(1,row+1): #range(1,4) 1,2,3
        print(chr(64+row),end=' ')
    print()
