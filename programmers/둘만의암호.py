from string import ascii_lowercase


def solution(s, skip, index):
    answer = ''
    alphabet_list = list(ascii_lowercase)

    for i in skip:
        alphabet_list.remove(i)

    size = len(alphabet_list)

    for i in s:
        answer_index = (alphabet_list.index(i) + index) % size
        answer += alphabet_list[answer_index]
    return answer
