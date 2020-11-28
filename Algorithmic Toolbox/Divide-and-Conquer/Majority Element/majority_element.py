# python3

import collections
def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
#        assert len(elements) <= 10 ** 5
    count = collections.Counter(elements)
    max_el = max(count.keys(), key=count.get)
    if count[max_el] > len(elements)/2:
        return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
