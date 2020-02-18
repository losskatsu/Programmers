# 100 점

def solution(heights):
    answer = [0]*len(heights)    
    while heights:
        last_top = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if(last_top < heights[i]):
                answer[len(heights)] = i+1
                break            
    return answer
