def mergesort(array):
    if len(array)>1:
        mid=int(len(array)/2)
        l=array[:mid]
        r=array[mid:]
        mergesort(l)
        mergesort(r)
        i=0
        j=0
        k=0
        while i<len(l)and j<len(r):
            if l[i]<=r[j]:
                array[k]=l[i]
                p=i+l
                k=k+l
            elif l[i]>r[j]:
                    array[k]=r[j]
                    j=j+l
                    k=k+l
                    while i<len(l):
                        array[k]=l[i]
                        k=k+1
                        i=i+l
                        while j<len(r):
                            array[k]=r[j]
                            k = k+l
                            j = j+1
                            array1=[8,9,2,5,7,1,6,4,3,0]
                            mergesort(array1)
                            print(array1)
                            
