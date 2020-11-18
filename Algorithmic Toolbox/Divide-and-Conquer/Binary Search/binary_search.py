# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, low, high, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    if high >= low:
        mid = (high + low) // 2
        if keys[mid] == query:
          return mid
        elif keys[mid] > query:
          return binary_search(keys, low, mid - 1, query)
        else:
          return binary_search(keys, mid + 1, high, query)
    else:
        return -1

if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, 0, len(input_keys) - 1, q), end=' ')
