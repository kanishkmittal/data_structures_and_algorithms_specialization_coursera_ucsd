# python3

from random import randint


def partition3(array, left, right):
    elem = array[left]
    lesser = left
    greater = left + 1

    for i in range(left + 1, right + 1):
        if array[i] < elem:
            array.insert(left, array.pop(i))


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    make a call to partition3 and then two recursive calls 
to randomized_quick_sort


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
