import numpy
mylist=[1.5,3,28,False] #hetrogenous:data->mix type
myarray=numpy.array(mylist) #homogenous:data->similar type 
print(myarray,type(myarray[0]))
print(mylist,type(mylist[0]))