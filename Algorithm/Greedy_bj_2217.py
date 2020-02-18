
'''
N(1≤N≤100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다. 단, 각각의 로프는 한 개씩만 존재한다.
'''

# 로프 갯수 입력 받음
N = int(input())

# 로프 무게를 입력받아 내림차순 정렬
ropeList = sorted([int(input()) for i in range(N)],
                reverse=True)

# 현재 문제에서 최적의 선택 = 최대한 무거운 무게를 들 수 있는 경우
# 최적 선택의 기준 = 주어진 로프 각각의 중량보다 무거운 무게는 들 수 없음
# 상식적으로 중량이 무거운 경우의 줄들이 더 무거운 무게를 들 수 있음 
# 만약 가벼운 중량의 로프가 들어온다면, 그 로프 중량이 1/n 무게를 초과할 가능성이 높음
# 따라서 무게가 무거운 순서로 정렬 후 조건식 작성

k = 0
w = 0
chosen = []
result = []
for rope_weight in ropeList:
    w = w + rope_weight   # 전체 무게
    k = k + 1             # 로프 갯수
    p = w/k               # 로프 하나가 견딜 평균 무게
    if rope_weight < p:                 # 만약, 새로 선택하는 로프의 중량이 평균무게보다 가볍다면 
        total_weight = rope_weight*k    # 전체 무게는 새로 선택하는 로프 중량 * 로프 갯수 
        result.append(total_weight)     # (새로 선택되는 로프 중량보다 무겁게 들 수 없기 때문에) 전체 무게 저장
    else:
        chosen.append(rope_weight)      # 만약, 새로 선택하는 로프의 중량이 평균무게보다 무겁거나 같다면
        total_weight = sum(chosen)      # 전체 무게는 각 로프 중량을 다 더한 값
        result.append(total_weight)     # 전체 무게 저장

print(max(result))   # 저장된 전체 무게 중 max 출력
