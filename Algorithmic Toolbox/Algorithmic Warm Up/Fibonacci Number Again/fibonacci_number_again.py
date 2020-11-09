# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def pisano_period(m):
    prev, curr = 0, 1
    for i in range(m * m):
        prev, curr = curr, (prev + curr) % m
        if (prev == 0 and curr == 1):
            return i + 1


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    period = pisano_period(m)
    n = n % period
    if n <= 1:
        return n
    fib = [None] * (n + 1)
    fib[0], fib[1] = 0, 1
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % m
    return fib[n]

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
