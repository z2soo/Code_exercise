#트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다. 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

bridge_length = int(input())
weight = int(input())
truck_weights = list(map(int, input().split()))

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = [0] * bridge_length
    truck_weights.reverse()
    truck = truck_weights.pop()

    while True:
        cnt = cnt+1

        if sum(bridge[1:]) + truck <= weight:        
            for k in range(len(bridge)):
                if k+1 == len(bridge):
                    bridge[-1] = truck
                else:
                    bridge[k] = bridge[k+1]

            if len(truck_weights) != 0:
                truck = truck_weights.pop()

            else:    
                truck = 0
                
        else: 
            for k in range(len(bridge)):
                if k+1 == len(bridge):
                    bridge[-1] = 0
                else:
                    bridge[k] = bridge[k+1]
        
        if len(truck_weights)*bridge_length <= cnt and sum(bridge) == 0:
            break
        
    return cnt
















        
       
        
    return cnt

print(solution(bridge_length, weight, truck_weights))