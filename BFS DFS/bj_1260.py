'''
정점의 개수 N
간선의 개수 M
탐색을 시작할 정점의 번호 V
'''

# 입력받기 
N, M, V = map(int, input().split())
myList = [[] for _ in range (N+1)]      

# 각 정점이 연결된 값을 넣어주고 sort 
for _ in range(M):
    a, b = map(int, input().split())  #간선이 연결하는 두 정점 번호
    myList[a].append(b)
    myList[b].append(a)
for _ in myList:
    _.sort()
print(myList)


# DFS 탐색: 이건 무조건 1번부터 시작하는 함수 
def dfs():
    global V, M, N
    stack = []
    visited = []
    #visited.append(V)
    #stack.append(V)
    #for _ in range(1, N+1):           #정점 개수만큼  
        for k in myList[_]:           #각 정점에 연결된 정점 리스트
            if k not in visited:
                stack.append(k)
        while stack:
            current = stack.pop() 
            if current not in visited:
                visited.append(current)
    return(visited)
print(dfs())
        


# BFS 탐색: 하나 정점에서 간선 다 구하고 넘어감


