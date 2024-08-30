def maxAndMin(numbers):
    max = numbers[0]
    min = numbers[0]

    for i in numbers:
        if i > max:
            max = i
        elif i < min:
            min = i

    return [min, max]


print(maxAndMin([2, 4, 1, 0, 2, -1]))
print(maxAndMin([20, 50, 12, 6, 14, 8]))
print(maxAndMin([100, -100]))
