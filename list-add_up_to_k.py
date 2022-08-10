arr=[3,5,7,10]
k=17
flag=False
hashset = set()
for i in range(0,len(arr)):
    if k-arr[i] in hashset:
      flag=True
    hashset.add(arr[i])
print( flag )
