'''정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V. 
간선이 연결하는 두 정점의 번호. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.'''

N, M, V = map(int, input().split())
myList = [[] for _ in range (N+1)]      #각 정점이 연결된 값을 넣을 리스트



#각 정점이 연결된 값을 넣어줌 
for _ in range(M):
    a, b = map(int, input().split())  #간선이 연결하는 두 정점 번호
    if b not in myList[a]:
        myList[a].append(b)
    if a not in myList[b]:      #이 부분 빠지면 일방향 연결로 정점 번호 저장
        myList[b].append(a)
    else:
        pass

for _ in myList:
    _.sort()
print(f'연결된 정점: {myList}') 







# # DFS 탐색: 타고 타고 들어감
# visited = []                        #방문한 정점 번호 저장할 리스트
# nodeList = [_ for _ in range(1,M)]     #존재하는 정점 번호 리스트
# print(f'정점 리스트: {nodeList}')


   
# def func_d():
#     global N,M,V,nodeList
#     while len(nodeList) != 0:
#         if V not in visited:
#             t = V
#             nodeList.remove(V)
#             if t not in visited:
#                 visited.append(t)
#         else:   
#             t = nodeList.pop(0)
#             if t not in visited:
#                 visited.append(t)
#         print(f'방문하는 노드:{t}')
#         nodeList = myList[t]
#         print(f'남은 노드:{nodeList}')
#         func_d()
#     return(visited)


# print(func_d())


        


# # BFS 탐색: 하나 정점에서 간선 다 구하고 넘어감
