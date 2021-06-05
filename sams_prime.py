def pos_sum(arr, pos1, pos2):
    if pos1 == 0:
        #print(arr[pos2])
        return arr[pos2]
    #print(arr[pos2] - arr[pos1])
    return arr[pos2] - arr[pos1]

def cum(A):
    sumA = A.copy()
    for i in range(1, len(sumA)):
        sumA[i] = (sumA[i-1] + sumA[i])
    return sumA
    
def isprime(num):
    if num == 1:
        return False
    if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               return False
       else:  
           return True
    else:  
       return True

def prime_sum(A):
    for j in range(len(A)):
        if not isprime(A[j]):
            A[j] = 0 
    #print(A)
    sumA = cum(A)
    N = len(sumA)
    
    for i in range(1,N):
        left_sum = sumA[i-1]
        right_sum = sumA[N-1] - sumA[i]
        
        #print(left_sum)
        #print(right_sum)
        
        if (left_sum==right_sum):
            return i
    return 0
          
T = int(input()) # Test Cases

for i in range(T):
    array_length = int(input())
    A = list(map(int, input().strip().split()))
    answer = prime_sum(A)
    print(answer)
