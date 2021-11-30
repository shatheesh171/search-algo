def linearSearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1

arr=[20,30,40,50,90]
print(linearSearch(arr,30))