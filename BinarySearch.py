def binarySearch(array,value):
    start=0
    end=len(array)-1
    middle=int((start+end)/2)
    while start<=end:
        if value==array[middle]:
            return middle
        elif value<array[middle]:
            end=middle-1
        else:
            start=middle+1
        middle=int((start+end)/2)
    return -1

arr=[20,30,40,50,90,100,101]
print(binarySearch(arr,90))