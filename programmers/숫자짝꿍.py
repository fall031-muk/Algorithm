import collections

def solution(X, Y):
    answer = []
    x_counter = collections.Counter(X)
    y_counter = collections.Counter(Y)
    common = x_counter&y_counter
    common_keys = x_counter&y_counter.keys()
    answer_list = [int(k) for k in common_keys if common[k] > 0]
    answer_list.sort(reverse=True)
    if len(answer_list) == 0:
        return "-1"
    if len(set(answer_list)) == 1 and answer_list[0] == 0:
        return "0"
    return ''.join(str(n) * common[str(n)] for n in answer_list)