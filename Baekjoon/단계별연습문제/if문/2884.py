H, M = map(int, input().split())

# 45분 일찍 알람 설정
# 24시 넘어가는 경우 유의
def early45(H,M):
    if M-45 >= 0:
        M = M-45
        return (H,M)
    else:
        if H !=0:
            H = H-1
            M = M+15
        else:
            if M-45 >= 0:
                H = 23
                M = M-45
            else:
                H = 23
                M = M+15
        return (H,M)

H, M = early45(H,M)
print(H, M)