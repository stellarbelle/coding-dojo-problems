import random
arr = []
for x in range(100):
    arr.append(random.randint(0, 1000))

count = len(arr) - 1
while count > 0:
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
    count -= 1

print arr
