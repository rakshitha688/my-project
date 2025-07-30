def bubblesor(array):
    for i in range(len(array)):
      for j in range(0,len(array)-i-1):
        if array[j]>array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
            data=[5,6,0,2,-1]
            bubblesort(data)
print('sorted array in ascending order')
print(data)
