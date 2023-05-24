from time import time

N = 512

A = [1 for x in range(N*N)]  
B = [1 for x in range(N*N)] 
C = [0 for x in range(N*N)]

start = time()

for i in range(0,N):
    posi = i * N
    for j in range(0,N):
        posj = j * N
        mult = 0
        for k in range(0,N):
            mult += A[posi + k] * B[posj + k]
        C[posi + j] = mult

# def printArray(arr):        
#     print('{', end='')
#     for i in range (N):
#         if (i>0):
#             print()
#         for j in range (N):
#             print('['+str(arr [i*N+j])+']', end='')
#     print('}')

stop = time()
print( stop - start) 

# printArray(C)
#printArray(B)
#printArray(C)
