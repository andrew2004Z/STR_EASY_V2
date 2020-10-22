def ft_count_words(sstr):
    count = 1
    for i in sstr:
        if i == ' ':
            count += 1
    return count
