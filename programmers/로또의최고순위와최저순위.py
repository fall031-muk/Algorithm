def solution(lottos, win_nums):
    answer = []
    win_count = 0
    zero_count = lottos.count(0)
    win_dict = [6, 6, 5, 4, 3, 2, 1]

    for i in lottos:
        if i in win_nums:
            win_count += 1

    answer.append(win_dict[win_count + zero_count])
    answer.append(win_dict[win_count])

    return answer