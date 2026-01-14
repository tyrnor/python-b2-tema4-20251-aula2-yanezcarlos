def median(data, key):
    values = []
    for entry in data:
        try:
            value = float(entry[key])
            values.append(value)
        except (ValueError, KeyError):
            continue

    values.sort()
    n = len(values)
    if n == 0:
        return None

    mid = n // 2
    if n % 2 == 0:
        median_value = (values[mid - 1] + values[mid]) / 2
    else:
        median_value = values[mid]

    return median_value
def mean(data, key):
    total = 0
    count = 0
    for entry in data:
        try:
            value = float(entry[key])
            total += value
            count += 1
        except (ValueError, KeyError):
            continue

    if count == 0:
        return None

    return total / count