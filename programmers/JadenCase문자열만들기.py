def solution(s):
    words = []
    split_s = s.split(' ')
    print(split_s)
    for i in split_s:
        if i == '':
            words.append(i)
        else:
            words.append(i[0].upper()+i[1:].lower())
    return ' '.join(words)
