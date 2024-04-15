def countFrequency(arr):
    count = 0
    arrnew = []
    for i in range(len(arr)-1):
        if(arr[i]== arr[i-1]):
             continue
        if(arr[i]!= arr[i-1]):
             for j in range(len(arr)-1):
                if(arr[i]==arr[j]):
                    count= count +1
        arrnew.append(arr[i])
        arrnew.append(count)
        count = 0
    return arrnew
array = [1,23,23,1,5,5,6]
x = countFrequency(array)
print(x)

        