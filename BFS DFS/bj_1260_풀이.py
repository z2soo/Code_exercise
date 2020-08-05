
# 2. DFS 메소드
# DFS를 재귀로 구현할 경우 종료조건이 가장 중요하다. (무한루프를 돌 수 있기때문이다.)
# 때문에 DFS를 구현할때는 항상 종료조건부터 작성하자.
def dfs(V,visited,result):
    # 이미 방문한 정점이라면 되돌아간다.
    if visited[V] == 1 : return
    
    # 방문한 적이 없으면 돌아가지 않으니 아래 코드들이 수행된다.
    
    # 현재 방문한 노트를 방문체크해준다.
    visited[V] = 1
    
    # 결과에 현재 정점을 넣어준다. 결과는 방문한 순서를 저장하는 배열이다.
    result.append(V)
    
    # 현재 정점의 간선정보를 받아온다.
    for num in line[V]:
        # 이후 그 번호로 dfs 메소드를 재귀해준다
        dfs(num,visited,result)





# 3. BFS 메소드
def bfs(V,visited,result):
    # Queue를 선언해준다.
    queue = []
    
    # 만들어진 큐에 현재 정점을 넣는다.
    queue.append(V)
    
    # 시작 정점 방문체크
    visited[V] = 1

    
    
    # 이후 큐가 비워질 때 까지 수행한다. 더 이상 방문할 곳이 없으면 큐는 비워진다.
    while queue:
        # 현재 정점이 무엇인지 확인하기위해 큐에서 꺼낸다.
        now = queue.pop(0) # pop() 메소드에 꼭 매개변수 0을 전달해야 큐가 구현된다. 큐는 선입선출이다.
        # 결과에 현재 정점을 넣어준다.
        result.append(now)        
        
        # 그 다음 현재 번호의 연결된 정점들을 가져온다.
        for num in line[now]:
            
            # 만약 이미 방문한 정점이 아니라면 큐에 그 정점들을 모두 넣어준다.
            if visited[num] != 1 : 
                queue.append(num)
                # 방문체크는 큐에 넣어줄때 해야한다. 아니면 중복될 수도 있다.
                visited[num] = 1
    


# Main 함수, 입력을 받고 DFS, BFS 메소드를 호출함.

# 1. 입력받기
# N: 정점의 개수, M: 간선의 개수, V: 시작 번호
N, M, V = map(int,input().split())

# 1-1. 간선정보를 담을 변수 선언
line = [[] for _ in range(N+1)] # 정점이 0이 아닌 1부터 시작하므로 N+1만큼 생성해줌, (0번째 인덱스는 사용 안함) 

# 1-2. 이후 간선(M)의 개수만큼 간선정보를 입력받음.
for _ in range(M):
    num1, num2 = map(int,input().split())
    line[num1].append(num2) # 간선은 양방향이니 두 정점 모두에 간선정보를 입력시켜야함.
    line[num2].append(num1) # num1 정점에서 num2로, num2 정점에서도 num1로 갈 수 있어야함.

# 1-3. 문제에서는 한 정점에서 갈 수 있는 정점이 여러개일때 작은 번호부터 탐색하라고 되어있음, 
#      입력에는 높은 번호가 우선 입력되는 경우가 있을 수 있으므로 이를 정렬해주어야함.
for num in line:
    num.sort()

# 1-4. 탐색여부를 저장할 배열 하나를 생성해준다.
visited = [0 for _ in range(N+1)] # 간선이 1부터 시작하니 편하게 하기 위해 N+1만큼 생성!

# 1-5. 결과를 출력할 배열 하나를 생성해준다.
result = []


#2. DFS 수행
dfs(V,visited,result)
for num in result:
    print(num, end = " ")


print()
#3. BFS를 수행하기 전에 result와 visited 를 꼭 초기화해줘야한다.
result = [] 
visited = [0 for _ in range(N+1)]

#4. BFS 수행
bfs(V,visited,result)
for num in result:
    print(num, end = " ")