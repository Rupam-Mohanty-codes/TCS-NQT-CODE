def findSmallest(arr):
   smallest = 100000000
   for i in range(len(arr)) :
      if(arr[i] < smallest):
         smallest = arr[i]
   return smallest

array = [1,5,34,76,3456,10]
x = findSmallest(array)
print(x)

    


