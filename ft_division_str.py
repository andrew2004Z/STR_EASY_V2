def ft_len(sstr):
    l = 0
    for i in sstr:
        l += 1
    return l


def  ft_division_str(sstr):
    if ft_len(sstr) % 2 == 0:
        i = 0
        s1 = ''
        s2 = ''
        s3 = ''
        while i != ft_len(sstr)//2:
            s1 += sstr[i]
            i +=1
        while i < ft_len(sstr):
            s2 += sstr[i]
            i += 1
        s3 = s2 + s1
    else:
        i = 0
        s1 = ''
        s2 = ''
        s3 = ''
        while i != (ft_len(sstr) + 1) // 2:
            s1 += sstr[i]
            i += 1
        while i < ft_len(sstr):
            s2 += sstr[i]
            i += 1
        s3 = s2 + s1
    return s3
