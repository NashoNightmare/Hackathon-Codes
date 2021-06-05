T = int(input()) #Testcases

for i in range(T):
    n = int(input()) # number of students
    arr = list(map(int, input().strip().split()))
    arr.sort()
    total = 0
    k = 0
    stacked = -1
    for j in range(len(arr)):
        if (arr[j] == stacked):
            total += k
        else:
            k += 1
            total += k
        stacked = arr[j]
    print(total)

        
