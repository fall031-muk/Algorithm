def solution(N, stages):
    dic = {}
    stages.sort()
    count = len(stages)
    for i in range(1, N+1):
        if count == 0:
            dic[i] = 0
        else:
            s_count = stages.count(i)
            dic[i] = s_count/count
            count -= s_count
    sort_dic = sorted(dic, key=dic.get, reverse=True)
    return sort_dic

    # 아래코드: key, values 값 반환 후 key값만 뽑아서 return
    # sort_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    # return [i[0] for i in sort_dic]
