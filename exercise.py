from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [A, B]
print(list(product(*C)))
