def ft_len(sstr):
    l = 0
    for i in sstr:
        l += 1
    return l


def ft_change_place_word(sstr):
    i = 0
    s1=''
    s2 =''
    s3 = ''
    while sstr[i] != ' ':
        s1 += sstr[i]
        i+=1
    i+=1
    while i < ft_len(sstr):
        s2 += sstr[i]
        i += 1
        s3 = s2 + ' ' +s1
    return s3
