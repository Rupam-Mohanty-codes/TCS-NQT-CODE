def largest(arr):
    large = arr[0]
    for i in range(len(arr)):
        if ( arr[i]>large):
            large = arr[i]
    return large

array = [2,23,45,67,54,234,1234]
x = largest(array)
print(x)