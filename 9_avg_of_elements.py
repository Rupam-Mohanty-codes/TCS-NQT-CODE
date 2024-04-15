def findAvg(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    avg = sum /(len(arr))
    return avg
array = [1,2,3,4,5]
x = findAvg(array)
print("the average is ",x)