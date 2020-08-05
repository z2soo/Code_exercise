'''
컴퓨터 개수: N
연결 정보: M
1번 컴퓨터를 통해 바이러스 걸리는 컴퓨터 번호 
'''

N = int(input())
M = int(input())
myList = [[] for _ in range(M)]

for _ in range(M):
    a,b = map(list, int(input()))
    myList[a].append(b)
    myList[b].append(a)

for _ in myList:
    _.sort

print(myList)