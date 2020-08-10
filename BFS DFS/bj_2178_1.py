'''N×M크기의 배열로 표현되는 미로

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

1: 이동할 수 있는 칸, 0: 이동할 수 없는 칸
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동
칸을 셀 때에는 시작 위치와 도착 위치도 포함

입력
첫째 줄에 두 정수 N, M 
다음 N개의 줄에는 M개의 정수로 미로

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력
'''
'''
(1, 1) : 시작 
(N, M) : 목표
myList : 미로
'''

# 입력받기
N, M = map(int, input().split())
myList = []
for _ in range(N):
    m = list(input())
    m = [int(_) for _ in m]
    myList.append(m)

# 방문 유무 표시 
visited = [[0 for _ in range(M)] for i in range(N)]
result = [[0 for _ in range(M)] for i in range(N)]

# 방향키
directions = (0,1),(1,0),(-1,0),(0,-1)

# 함수 생성
def miro():
    global N, M, myList, directions
    que = []
    que.append((0,0))
    result[0][0] = 1
    while que:
        x, y = que.pop(0)
        for dx, dy in directions:
            xt = x + dx
            yt = y + dy
            if xt < 0 or yt < 0 or xt > N-1 or yt > M-1:
                #범위를 벗어난 경우 처리
                pass
            else:
                if visited[xt][yt] == 0 and myList[xt][yt] == 1:
                    visited[xt][yt] = 1                #방문처리
                    result[xt][yt] = result[x][y] +1   #내가 헤맨 곳
                    que.append((xt,yt))
    return(result[N-1][M-1])            
print(miro())

# 내가 헤맨 곳
# 1. 시작 지점부터 1 이동으로 간주하는 것
# 2. cnt 변수 따로 만들어서 이동수 체크함: 오류: 이전 방문수+1로 해결