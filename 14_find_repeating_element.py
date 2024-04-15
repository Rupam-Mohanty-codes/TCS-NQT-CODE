def findrepeating(arr):
    dictnew={}
    arrnew =[]
    for i in arr:
        if i in dictnew:
            dictnew[i] += 1 
        else :
            dictnew[i] = 1
    for i ,count in dictnew.items():
        if(count > 1):
            arrnew.append(i)
    return arrnew
arr = [1, 2, 3, 4, 2, 3, 5, 5, 6]
x = findrepeating(arr)
print(x)
