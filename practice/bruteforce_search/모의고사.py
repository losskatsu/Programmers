# 100점

def solution(answers):
    final = []
    
    answer = [0]*3
    person1 = [1,2,3,4,5]
    n1 = len(person1)
    person2 = [2,1,2,3,2,4,2,5]
    n2 = len(person2)
    person3 = [3,3,1,1,2,2,4,4,5,5]
    n3 = len(person3)
    person = [person1, person2, person3]
    length = [n1, n2, n3]
    
    for i in range(0, 3):
        for j in range(0, len(answers)):
            idx_person = j%length[i]
            if(person[i][idx_person] == answers[j]):
                answer[i] += 1
    
    top_score = max(answer)
    for i in range(0, 3):
        if(answer[i] == top_score):
            final.append(i+1)
    
    return final
