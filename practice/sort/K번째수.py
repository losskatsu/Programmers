# 100 점

def solution(array, commands):
    answer = []
    n = len(commands)
    for i in commands:
        tmp_array = []
        init = i[0]-1
        end = i[1]
        n_ch = i[2]-1
        for j in range(init, end):
            tmp_array.append(array[j])
        tmp_array.sort()
        print(tmp_array)
        answer.append(tmp_array[n_ch])            
    return answer
