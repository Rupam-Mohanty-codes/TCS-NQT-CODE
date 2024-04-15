def rearrange(arr):
    arr.sort()
    size=len(arr)-1
    fs=size // 2
    for i in range(fs+1):
        print(arr[i])
    while(size >fs):
        print(arr[size])
        size -= 1

arr=[1,2,3,4,5,6]
rearrange(arr)


    