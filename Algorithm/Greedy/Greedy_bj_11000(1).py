'''수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
'''
N = int(input())
time_list = sorted( [ list(map(int, input().split())) for i in range(N) ], 
                    key = lambda x : (x[1], x[0]))

def find(time_list):
    time_list = time_list
    time = 0
    for meeting in time_list:
        if time <= meeting[0]:
            time = meeting[1] 
            time_list.remove(meeting)
    return(time_list)

cnt = 0
while True:
    var = find(time_list)
    cnt = cnt+1
    time_list = var
    if len(time_list) == 0:
        print(cnt)
        break