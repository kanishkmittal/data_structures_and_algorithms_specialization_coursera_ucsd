# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    stops.append(d)

    num_refills = 0
    current_stop = 0
    last_stop_val = 0
    while current_stop < len(stops):
        if stops[current_stop] - last_stop_val <= m:
            current_stop += 1
            continue
        elif stops[current_stop] - stops[current_stop - 1] > m or current_stop == 0:
            return -1
        else:
            last_stop_val = stops[current_stop - 1]
            num_refills += 1
    return num_refills



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
