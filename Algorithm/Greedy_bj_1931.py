n = int(input())
time_list = sorted([list(map(int, input().split(' '))) for i in range(n)], key=lambda x : (x[1], x[0]))


def cnt_meeting(time_list):
    cnt = 0
    time = 0
    for meeting in time_list:
        if time <= meeting[0]:
            time = meeting[1] 
            cnt = cnt+1
    return(cnt)

print(cnt_meeting(time_list))

######################################

    import sys

    N = int(sys.stdin.readline())
    meeting = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)], key=lambda x: (x[1], x[0]))

    end = answer = 0
    for m in meeting:
        if end <= m[0]:
            end = m[1]
            answer += 1
    print(answer)
