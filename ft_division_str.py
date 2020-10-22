def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_division_str(str):
    if ft_len(str) % 2 == 0:
        i = 0
        s1 = ''
        s2 = ''
        s3 = ''
        while i != ft_len(str) // 2:
            s1 += str[i]
            i += 1
        while i < ft_len(str):
            s2 += str[i]
            i += 1
        s3 = s2 + s1

    else:
        i = 0
        s1 = ''
        s2 = ''
        s3 = ''
        while i != (ft_len(str) + 1) // 2:
            s1 += str[i]
            i += 1
        while i < ft_len(str):
            s2 += str[i]
            i += 1
        s3 = s2 + s1
    return s3
