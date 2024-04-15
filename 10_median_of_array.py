def findMedian(arr):
    arr.sort()
    size = len(arr)

    if size % 2 != 0:
        return arr[size // 2]
    else:
        num1 = (size // 2) - 1
        num2 = size // 2
        mid = arr[num1] + arr[num2]
        mid = mid / 2
        return mid

array = [1, 2, 3, 4, 5]
x = findMedian(array)
print(x)
