from sys import stdin
from collections import deque

'''
walk: x-1, x+1로 이동
jump: 2*x로 이동

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후?
'''  


 
N, K = map(int, input().split())
visited = [0 for _ in range(100,000)]
que = []
print(visited)
# 방문한 지점을 넣어주고, K가 append 되는 순간 종료 및 마지막에 방문 지점 length-1 출력

# direction = x+1, x-1, x*2

def seek():
    global N, K
    que.append(N)
    while que:
        x = que.pop(0)
        # visited[x] = 1
        direction = x+1, x-1, x*2
        for key in direction:
            nextX = key
            que.append(nextX)
            # print(que)
            if nextX == K:
                break
                
            

print(seek())


