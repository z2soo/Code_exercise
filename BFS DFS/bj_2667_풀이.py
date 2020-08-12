
# Encoding: UTF-8

# 2. 알고리즘 구현

# grid의 한 점이 1이었을 경우 메소드로 진입한다.
# 1을 기준으로 BFS 탐색하여 갈 수 있는 모든 1의 공간을 -1로 변경해준다.
# 메소드를 리턴하기 전 houseSize 변수에 이 단지의 크기를 저장해준다.
def housing(grid, point):
    # 먼저 houseSize 변수를 global로 사용한다. 맵의 사이즈를 알면 편하니 N도 같이 쓴다.
    global houseSize, N
    
    
    # BFS 탐색을 위한 큐를 선언해준다.
    queue = []
    
    # 큐에 현재 위치를 넣어준다.
    queue.append(point)
    nowx, nowy = point
    # 현재 위치의 grid값을 -1로 바꾼다. 이는 visit와 비슷한 로직을 내기 위함이다.
    grid[nowx][nowy] = -1
    
    # 단지의 크기를 위한 변수를 선언해준다. 메소드에 진입한 것 자채로 단지가 존재하므로
    # 사이즈는 1부터 시작하면 된다.
    size = 1
    
    
    # 방향키를 위한 변수 설정.
    directions = (1, 0), (0, 1), (-1, 0), (0, -1)
    
    
    # 큐가 비워질 때 까지 (더이상 인접한 1인 지점이 없을 때 까지) 수행한다.
    while queue:
        # 큐에서 뽑아낸 값이 현재 위치다.
        nowx, nowy = queue.pop(0)
        
        # 현재 위치로부터 4방향을 탐색한다.
        for dx, dy in directions:
            nextx = nowx + dx
            nexty = nowy + dy
    
            # 다음 위치가 grid 배열 범위 안이고,
            # grid의 값이 1일 때에만 진입한다.
            if 0 <= nextx < N and 0 <= nexty < N and grid[nextx][nexty] == 1:
                
                # 위 조건을 만족하면 인접한 1인 경우다. 해당 위치를 큐에 넣어준다.
                queue.append((nextx,nexty))
                
                # 해당 위치의 grid값을 -1로 바꾼다.
                grid[nextx][nexty] = -1
                
                # 집이 한 채 더있는 셈이니 size를 1 올려준다.
                size += 1
                
                
    # 큐가 모두 비워지면 여기로 온다.
    # 메소드가 종료되기 전에 size 값을 houseSize 변수에 넣어주면 된다.
    houseSize.append(size)            
                




                
# Main 함수
# 1. 입력받기
N = int(input())

# N * N 의 지도 생성
grid = [list(map(int, input())) for _ in range(N)]

# 단지의 개수를 구하기 위한 변수
count = 0

# 각 단지의 크기를 저장하기 위한 리스트
houseSize = []

# grid 배열을 인덱스로 탐색한다.
for i in range(N):
    for j in range(N):
        # 만약 한 점이 처음에 입력받은 값 (1) 그대로라면 메소드를 수행해준다.
        # 호출되는 메소드는 한 점이 1인 경우 그 지점으로부터 BFS로 뻗어나가 전부 다른 숫자로 바꿔준다.
        # grid[i][j]의 1값을 -1로 바꿀 예정이다. 때문에 같은 단지내에서 중복실행되는 경우는 없다.
        # 한 번 들어갔을때 spot과 인접한 갈수있는 모든 1의 영역을 모두 -1로 바꿔주기 때문이다.
        if grid[i][j] == 1:
            housing(grid, (i, j))
            # 메소드로의 진입은 단지의 진입을 의미하므로 count를 1 늘려준다
            count += 1


    # 맨 위 메소드 (2번) 으로 가세요



# 3. 결과 출력하기

# 집의 개수 출력
print(count)
# 먼저 집의 수를 오름차순으로 정렬한다. (문제 요구사항)
houseSize.sort()
# 그다음 순차적으로 출력해준다.
for result in houseSize:
    print(result)
