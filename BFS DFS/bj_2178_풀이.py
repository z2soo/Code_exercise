
#Encoding: UTF-8


# 2. 알고리즘 수행
def find(grid):
    # 배열의 최대범위를 알아야하기 때문에 N,M을 전역변수로 사용함. (매개변수로 받아도 무방함)
    global N,M
    
    # 2차원 배열을 이동하기위해 이동방향키를 설정해줌
    directions = (1, 0), (0, 1), (-1, 0), (0, -1)
    # 결과를 저장할 (이동횟수를 저장할) 배열 하나를 만들어줌
    result = [[0 for _ in range(M)] for _ in range(N)]
    result[0][0] = 1
    
    
    # 최단거리는 BFS로 푸는게 좋음. BFS로 풀기 위해 큐를 생성함.
    queue = []
    
    # 큐에 시작지점을 넣어줌. 문제에서 시작지점은 항상 (0, 0)임.
    queue.append((0,0))
    
    # 방문체크를 위해 2차원 배열을 하나 더 만들어줌.
    visited = [[0 for _ in range(M)]for _ in range(N)]
    
    # 현재 시작점 방문체크해줌
    visited[0][0] = 1
    
    
    
    # 큐를 돌려줌
    while queue:
        # 현재 큐에 들어가있는 행, 열 값을 받아냄
        nowx, nowy = queue.pop(0)
        # 현재 위치에서 네 방향을 탐색해줌
        for dx, dy in directions:
            nextx = nowx + dx
            nexty = nowy + dy
            
            # nextx, nexty 값이 배열범위 안에 있을때만 탐색을 수행함. 이렇게 안하면 index 초과 오류남
            if 0 <= nextx < N and 0 <= nexty < M:
                
                # 벽이 아니거나 (grid가 1이거나) 방문하지 않았을 때 (visit가 0일때) 에만 탐색을 수행함
                if grid[nextx][nexty] == 1 and visited[nextx][nexty] == 0:
                    
                    # 벽이 아니거나 방문하지 않았으면 큐에 넣어줌
                    queue.append((nextx, nexty))
                    # 방문체크해줌
                    visited[nextx][nexty] = 1
                    # 이동거리를 체크해줌, 이동거리는 현재지점 + 1로하면 계속해서 늘어남
                    result[nextx][nexty] = result[nowx][nowy] + 1
            
    
    # 도착지점인 (N-1, M-1) 지점의 이동거리를 반환해줌
    return result[N-1][M-1]
    
    
    
    
# Main 함수

# 1. 입력받기

# 1-1. N과 M 입력받기
N, M = map(int, input().split())
# 1-2. 지도(Grid) 입력받기, 다음은 공백없는 여러 줄의 입력을 2차원 배열로 입력받는 코드임.
grid = [list(map(int,input())) for _ in range(N)]

# 1-3. 결과 출력하기(알고리즘을 수행하는 함수를 호출하고 결과를 리턴받자마자 출력시킴)
print(find(grid))