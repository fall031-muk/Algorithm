from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    buff = deque([0 for a in range(bridge_length)])
    # buff = [0] * bridge_length
    truck_weights = deque(truck_weights)
    total_weights = 0
    
    while len(buff):
        answer += 1
        total_weights -= buff.popleft()
        if truck_weights:
            if total_weights + truck_weights[0] <= weight:
                total_weights += truck_weights[0]
                buff.append(truck_weights.popleft())
                
            else:
                buff.append(0)
        
    return answer
