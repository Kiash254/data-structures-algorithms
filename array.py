print('@@@ Arrrys in data structures')

arr=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(arr)):
    print(arr[i])

#access elements in array
print('Access elements in array')
print(arr[0])

#insert array 
arr.insert(1, 90)
for x in arr:
    print(x)
#delete array
arr.remove(90)
for x in arr:
    print(x)
#search array
print('search array')
print(10 in arr)
#update array
print('update array')
arr[0]=100
for x in arr:
    print(x)