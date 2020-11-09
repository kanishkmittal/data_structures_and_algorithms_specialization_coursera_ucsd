# python3

def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    index_1 = 0
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] > numbers[index_1]:
            index_1 = i
    numbers[n - 1], numbers[index_1] = numbers[index_1], numbers[n - 1]
    index_2 = 0
    for i in range(1, n - 1):
        if numbers[i] > numbers[index_2]:
            index_2 = i
    numbers[n - 2], numbers[index_2] = numbers[index_2], numbers[n - 2]
    return numbers[n - 2] * numbers[n - 1]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
