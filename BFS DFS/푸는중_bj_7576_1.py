a  
import collections       #해당 문제는 디큐, 덱 사용; 기존 리스트는 멀티스레드

'''
하루 후, 익은 토마토 인접한 안익은 토마토가 익음
모든 토마토가 익을 때 까지 걸리는 최소 일 수
토마토가 들어있지 않을 수 있음

M: 상자 col
N: 상자 row
0: 안익음
1: 익음
-1: 없음

 
 
모든 토마토가 익는 최소 일 수 출력
저장시부터 모두 익은 상태: 0
모두 익지 못하는 상태: -1
'''
# # 필요한 정보 입력받음
# M,N = map(int, input().split())
# check = [[0 for _ in range(M)] for _ in range(N)]
# myBox = []

# # 토마토 상자 정보 입력받음
# for _ in range(N):
#     line = input().split(' ')
#     line = [int(_) for _ in line]
#     myBox.append(line)
# print(myBox)

# # 방향키 설정
# directions = (0,1),(0,-1),(1,0),(-1,0)

# # 함수 생성
# def tomato():
#     global directions, check, N, M, myBox
#     deq = collections.deque()    

#     for i in range(N):
#         for j in range(M):
#             if myBox[i][j] == 1:
#                 print(f'1인 좌표: {(i,j)}')
#                 deq.append((i,j))                   #우선 출발지점 넣어주기        
#     cnt = 0

#     while deq:
#         x, y = deq.popleft()                #deq에서 좌표 가져오기
#         if check[x][y] == 0 :            #방문하지 않았다면
#             check[x][y] = 1             #방문체크
            
            
#             for dx, dy in directions:   #주변 칸 좌표 확인
#                 newX = x + dx
#                 newY = y + dy
                
#                 if 0 <= newX < N and 0 <= newY < M and myBox[x][y] == 1: 
#                     if check[newX][newY] == 0:    
#                         print('추가:', (newX,newY))
#                         deq.append((newX, newY))      
#                         myBox[newX][newY] = 1
#                         cnt+=1    
#     return(cnt)





# 하루 동안 주위 토마토 익는 것: x,y 하나 동안 
def oneDay():
    global directions, check, N, M, myBox
    # deq = collections.deque()  

    # while deq:
    x, y =  deq.popleft()
    if check[x][y] == 0 :            #방문하지 않았다면
        check[x][y] = 1             #방문체크
        for dx, dy in directions:   #주변 칸 좌표 확인
            newX = x + dx
            newY = y + dy    
            if 0 <= newX < N and 0 <= newY < M and myBox[x][y] == 1: 
                if check[newX][newY] == 0:    
                    print('추가:', (newX,newY))
                    deq.append((newX, newY))      
                    myBox[newX][newY] = 1
# 하루 몇번이 반복되는지..?

# 지금 문제는 하루 지날때 cnt+1 되는게 아니라 한 칸이 1로 바뀔 때마다 cnt+1이 되고 있는 상태
# 함수 두개로 나눠야 하는거 같음...


# 확인했는데 익은 토마토면 = 1; 주위 접한 토마토 중 안익은 토마토=0 개수 확인
# 확인했는데 -1이면 없는 곳 

# 전체가 1이 되면 끝내기, 전체가 1이 되는데까지 날짜 출력
# 전체가 다 못 익을 경우면 -1 출력









# print(tomato()) 

# extend(): append랑 다르게 구분해서 추가 
# collections.deque.extendleft(): 좌측
# collections.deque.extend(): 우측

# pop()
# colections.deque.pop(): 우측
# colections.deque.popleft(): 좌측

