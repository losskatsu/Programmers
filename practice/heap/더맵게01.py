# 4점...테스트케이스는 통과함
# 정답보니가 heapq를 써야 시간제한 뚫을수있다고 하는데, 보통 이런 알고리즘쪽은 로직이 더 중요하지 않나.

def solution(scoville, K):
    answer = 0
    if(scoville[0] >= K):
        return answer
    while scoville:
        scoville.sort()
        low1 = scoville.pop(0)
        low2 = scoville.pop(0)
        newfood = low1 + (low2*2)
        answer += 1
        if(newfood >= K):
            return answer
        else:
            scoville.append(newfood)
    return
