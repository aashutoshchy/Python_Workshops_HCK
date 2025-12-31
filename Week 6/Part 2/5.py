def improved_average(a, b, c, d, e):
    numbers = [a, b, c, d, e]

    mean = sum(numbers) / 5

    numbers.sort()
    median = numbers[2]

    mode = numbers[0]
    max_count = 0
    for num in numbers:
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            mode = num

    return mode, median, mean
