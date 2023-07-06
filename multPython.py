import threading
from time import time

N = 512 # Tamaño de las matrices
threads = 2 # Cantidad de hilos

# Declaracion de las matrices
A = [1 for x in range(N*N)]  
B = [1 for x in range(N*N)] 
C = [0 for x in range(N*N)]

def printArray(arr):        
    print('{', end='')
    for i in range (N):
        if (i>0):
            print()
        for j in range (N):
            print('['+str(arr [i*N+j])+']', end='')
    print('}')

# Funcion que resuelve la multiplicacion
def mult(desde, hasta):
    for i in range(desde, hasta):
        posi = i * N
        for j in range(N):
            posj = j * N
            mult = 0
            for k in range(N):
                mult += A[posi + k] * B[posj + k]
            C[posi + j] = mult

thr = []

# Creacion de hilos
for i in range(threads):
    desde = int((N / threads) * i)
    hasta = int(desde + (N / threads))
    thr.append(threading.Thread(target=mult, args=(desde, hasta)))

start = time()

# Inician los hilos
for i in range(threads):
    thr[i].start()

# Se espera a que terminen todos los hilos
for i in range(threads):
    thr[i].join()

stop = time()

# Muestra el tiempo de ejecución
print("Tiempo de ejecución:", stop - start) 
