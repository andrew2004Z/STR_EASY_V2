def ft_len(sstr):
    l = 0
    for i in sstr:
        l += 1
    return l


def ft_cut_between_char(char, sstr):
    x = 0
    r = 0
    w = ''
    count = 0
    if char in sstr:
        for i in sstr:
            if i == char:
                count += 1
        if count == 1:
            return -1
        else:
            for i in range(ft_len(sstr)):
                if sstr[i] == char:
                    x = i
                    break
            for i in range(ft_len(sstr)):
                if sstr[i] == char:
                    r = i
            for i in range(x):
                w += sstr[i]
            r += 1
            while r < ft_len(str):
                w += sstr[r]
                r += 1
            return w
    else:
        return -2
