# python3

from random import randint


def partition3(a, left, right):
    elem = a[left]
    left_count = i = left
    right_count = right
    while i <= right_count:
        if a[i] < elem:
            a[i], a[left_count] = a[left_count], a[i]
            left_count += 1
            i += 1
        elif a[i] == elem:
            i += 1
        else:
            a[i], a[right_count] = a[right_count], a[i]
            right_count -= 1
    return left_count, right_count


def randomized_quick_sort(a, left, right):
    if left >= right:
        return
    pivot = randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    l, r = partition3(a, left, right)
    randomized_quick_sort(a, left, l - 1)
    randomized_quick_sort(a, r + 1, right)



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
