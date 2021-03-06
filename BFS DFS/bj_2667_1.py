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

# 연결 정보 입력 받음
for _ in range(N):
    m = list(input())
    m = [int(_) for _ in m]
    myList.append(m)


# 방향키: 좌, 우, 하, 상
directions = (0,1), (0,-1), (1,0), (-1,0)
que =[]


# 하나의 마을의 값을 받는 함수: 집이 몇 개 모여잇는지 출력
def home(point):
    global myList, directions, visited, N, que
    cnt = 1                                         #집 갯수 카운트 용
    que.append(point)
    tempx, tempy = point                            #오류2
    visited[tempx][tempy] = 1                                
    while que:
        x,y = que.pop(0)                            #현재 좌표 x,y
        for dx,dy in directions:    
            nextX = x + dx                          #인근 좌표 nextX, nextY
            nextY = y + dy                          
            if 0 <= nextX < N and 0 <= nextY < N and visited[nextX][nextY] == 0 and myList[nextX][nextY] == 1:
                visited[nextX][nextY] = 1
                que.append((nextX,nextY))
                cnt += 1
    return cnt 


# 전체 정보에서 마을이 몇 개 있는지 확인하는 함수
def village():
    result = []
    global myList, directions, N
    for a in range(N):
        for b in range(N):
            if visited[a][b] == 0 and myList[a][b] == 1:        #오류1
               point = (a,b)
               var = home(point)
               if var != 0:
                   result.append(var)
    return result


# 결과 프린트
final = village()
final.sort()                #오름차순 정렬
if len(final) == 0:         #마을이 없는 경우
    print(int(0))
else:
    print(len(final))
    for _ in final:
        print(_)


# 내가 막힌 부분
# 1. 한 번에 모든 좌표를 다 훑고 마을 갯수를 구하려고 했음; 실패
#    창혁오빠 코드 보고, 두 개의 함수로 나누어 생각 
# 2. 처음 생성한 home()은 (0,0)부터 시작하는 것, 어떻에 어느 좌표에서 시작하는지 알지?
#    방문 확인을 통해 한 번 방문한 곳은 다시 방문하지 않도록 함
# 3. 왜 오류나지?
#    반례) 3 \n101 \n010 \n101
#    오류1) myList[a][b] == 1 추가 작성; 방문한 적이 없으면서 방문하려는 좌표에 집이 있어야지 의미가 있기 때문
#    오류2) 