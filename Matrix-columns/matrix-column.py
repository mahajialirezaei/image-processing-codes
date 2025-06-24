import numpy as np


def getinput():
    n = int(input())
    a = []
    for i in range(n):
        a.append([])
        a[i] = list(map(float, input().split()))
    return a


def calculate_eigen(a:list):
    value, vector = np.linalg.eig(a)
    return value, vector

if __name__ == '__main__':
    a = getinput()
    val, vec = calculate_eigen(a)
    for item in val:
        print(f"{item:.3f}", end=" ")
    print()
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{vec[j][i]:.3f}", end=" ")
        print()