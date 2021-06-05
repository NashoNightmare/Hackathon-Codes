def cal_sum(sum_A, p, q):
    return sum_new(sum_A, q) - sum_new(sum_A,p)

def sum_new(sum_A, x):
    if x < 0:
        return 0
    else:
        return sum_A[x]

first_input = input()
N = int(first_input.strip().split()[0])
Q = int(first_input.strip().split()[1])

second_input = input()
A = list(map(int, second_input.strip().split()))

for i in range(1, len(A)):
    #A[i] = (A[i-1] + A[i])
    A[i] = sum(A[i-1:i+1])
    
p = 0
q = 0

for i in range(Q):
    query_line = input().split()
    p = int(query_line[0]) - 1
    q = int(query_line[1])   
    answer = cal_sum(A, p, q)
    print(answer)
    
