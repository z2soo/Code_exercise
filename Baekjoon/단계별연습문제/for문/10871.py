import sys

N, X = map(int, input().split())
myList = sys.stdin.readline().rstrip().split()

for i in range(N):
    k = int(myList[i])
    if k < X:        
        print(k, end=' ')
