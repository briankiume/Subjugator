from collections import Counter


def subjugator(a):
    counts = Counter(a)
    possible_dom = counts.most_common(1)[0]
    occurrences = possible_dom[1]
    dom_key = possible_dom[0]
    indexes = []
    if occurrences > (len(a) / 2):
        for x in range(len(a)):
            if a[x] == dom_key:
                indexes.append(x)
    else:
        indexes = -1

    return indexes


print(subjugator([3, 4, 3, 2, 3, -1, 3, 3]))
