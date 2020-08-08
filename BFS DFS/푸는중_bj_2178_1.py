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
print(myList)

# 필요한 내용
# (1,1)부터 시작
# 인근이 0인지 1인지 확인 및 저장? 카운트?
# (N,M)이 되면 멈춤


# 방문 유무 표시 
visited = [[0 for _ in range(M)] for i in range(N)]
result = [[0 for _ in range(M)] for i in range(N)]
print(visited)

cnt = 0
que = []

directions = (0,1),(0,1),(-1,0),(0,-1)


def miro():
    global N, M, myList
    que.append((1,1))
    cnt = 0
    while que:
        x, y = que.pop(0)
        print(x,y) 
        for dx, dy in directions:
            x = x + dx
            y = y + dy
            if x < 0 or y < 0:
                #범위를 벗어난 경우 처리
                print(x,y)
            if visited[x][y] == 0:
                visited[x][y] = 1  #방문처리
                if myList[x][y] = 0:
                #못지나가는 경우
                else:

                cnt += 1
                result[x][y] = cnt 

