def removeDuplicates(arr):
    arr.sort()
    i = 0 
    j = 1
    for j in range (len(arr)):
        if(arr[i]!=arr[j]):
            i = i +1
            arr[i]= arr[j]
    return i +1
arr = [1, 1, 2, 2, 2, 3, 3]
k = removeDuplicates(arr)
print("The array after removing duplicate elements is ")
for i in range(k):
        print(arr[i])
    