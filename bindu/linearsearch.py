def linearsearch(array,n,x):
    for i in range(,n):
      if(array[i]==x):
          return i
          return -1
array=[2,4,7,9,1]
x=1
n=len(array)
result=linearsearch(array,n,x)
if(result==-1):
  print("element not found:")
else:
     print("element found at index:",result)
