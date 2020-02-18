# 점수: 100점

def solution(participant, completion):
    answer = ''
    part_dic = {}
    uni_part = list(set(participant))
    
    comp_dic = {}
    uni_comp = list(set(completion))
    
    for person in uni_part:
        part_dic[person] = 0
    
    for person in participant:
        part_dic[person] += 1
    
    for person in uni_comp:
        comp_dic[person] = 0
    
    for person in completion:
        comp_dic[person] += 1
    
    for partkey in part_dic.keys():
        # for compkey in comp_dic.keys():
        #     if (partkey == compkey):
        #         if (part_dic[partkey] != comp_dic[compkey]):
        #             answer = partkey
        if partkey not in comp_dic.keys():
            answer = partkey
        
        if partkey in comp_dic.keys():
            if(part_dic[partkey] != comp_dic[partkey]):
                answer = partkey
    return answer
