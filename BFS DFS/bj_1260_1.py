'''
정점의 개수 N
간선의 개수 M
탐색을 시작할 정점의 번호 V
연결 간선 정보 myList
방문 정보 visited
큐 구조 que
결과 리스트 result
'''

# DFS
def dfs(V, myList, visited):
    if visited[V] == 0:             
        visited[V] = 1            
        result.append(V)             
        for node in myList[V]:       
            dfs(node, myList, visited)
    return(result)


def bfs(V, myList, visited):
    que = []
    que.append(V)
    while que:
        now = que.pop(0)
        if visited[now] == 0:
            visited[now] = 1
            result.append(now)
            for node in myList[now]:
                que.append(node)
    return(result)    


# 1. 입력받기 
N, M, V = map(int, input().split())
myList = [[] for _ in range (N+1)]      


# 2. 각 정점이 연결된 값을 넣어주고 sort 
for _ in range(M):
    a, b = map(int, input().split()) 
    myList[a].append(b)
    myList[b].append(a)
for _ in myList:
    _.sort()


# 3. 방문 정보, 결과
visited = [ 0 for _ in range(N+1) ]
result = []


#4. dfs bfs 결과(초기화 필수!)
dfs = dfs(V,myList,visited)
for i in dfs:
    print (i, end=' ')
print('')


visited = [ 0 for _ in range(N+1) ]
result = []
bfs = bfs(V,myList,visited)
for k in bfs:
    print (k, end=' ')

