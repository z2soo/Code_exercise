'''
1: 집이 있는 곳
0: 집이 없는 곳
연결된 집들의 모임 = 단지
단지의 총 수, 각 단지의 집 수(오름차순) 출력
'''

# 행, 열 갯수 입력 받음 
N = int(input())

# 연결 정보 저장용
myList = []

# 방문 표시 및 결과
visited = [[0 for _ in range(N)] for i in range(N)]
result = [[0 for _ in range(N)] for i in range(N)]

# 연결 정보 입력 받음
for _ in range(N):
    m = list(input())
    m = [int(_) for _ in m]
    myList.append(m)
print(myList) 

# 방향키: 좌, 우, 하, 상
directions = (0,1), (0,-1), (1,0), (-1,0)

# 좌표 하나씩 주위에 접한 집이 있는지 확인
# 접한 집이 있다면 같은 번호/문자로 result에 표시
# 접한 집 인근 또한 확인하기 위해 해당 좌표 append
# 방문 표시 
# 접한 집이 없다면 새로운 번호/문자로 reset하고 반복
# 번호로 묶음? 아니면 리스트로 생성?

def home():
    global myList, directions, visited
    que = []
    que.append((0,0))
    cnt = 1
    visited[0][0] = cnt
    if myList[0][0] == 1:
        result[0][0] = 1
    while que:
        print(que)
        x,y = que.pop(0)
        for dx,dy in directions:
            nextX = x + dx
            nextY = y + dy
            if 0 <= nextX < N and 0 <= nextY < N:       #index range 오류 확인
                if visited[nextX][nextY] == 0:          #방문한 적이 없다면
                    visited[nextX][nextY] = 1           #방문표시 해줌
                    que.append((nextX,nextY))           #que에 추가    
                    if myList[nextX][nextY] == 1:       #집이 있다면

################ 안되네?!?!??!?!?!?!?!?!?!?
                                                        #이전 집들과 연결되어 있다면
                                                        #동일한 값 cnt
                        if myList[x][y] == 1:
                            result[nextX][nextY] == cnt
                                                        #이전 집들과 떨어져 있다면
                                                        #cnt+1값
                        elif myList[x][y] == 0:
                            cnt = cnt+1
                            result[nextX][nextY] == cnt



    print(f'result\n{result}')
    print(f'visited\n{visited}')

home()


