def ft_len(sstr):
    l = 0
    for i in sstr:
        l += 1
    return l


def ft_analysis(sstr):
    print(sstr[2])
    print(sstr[ft_len(sstr) - 2])
    print(sstr[0], sstr[1], sstr[2], sstr[3], sstr[4], sep="")
    i = 0
    while i != ft_len(sstr) - 2:
        print(sstr[i], end="")
        i += 1
    i = 0
    print()
    while i != ft_len(sstr):
        if i % 2 == 0:
            print(sstr[i], end="")
        i += 1
    print()
    i = 0
    while i != ft_len(sstr):
        if i % 2 != 0:
            print(sstr[i], end="")
        i += 1
    print()
    i = 0
    while i != ft_len(sstr):
        print(sstr[ft_len(sstr) - i - 1], end="")
        i += 1
    print()
    i = 0
    while i != ft_len(sstr):
        if i % 2 == 0:
            print(sstr[ft_len(sstr) - i - 1], end="")
        i += 1
    print()
    print(ft_len(sstr))
