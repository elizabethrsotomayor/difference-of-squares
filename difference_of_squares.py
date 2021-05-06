def square_of_sum(number: int) -> int:
    total = 0
    for n in range(1, number + 1):
        total += n
    return total ** 2


def sum_of_squares(number: int) -> int:
    total = 0
    for n in range(1, number + 1):
        total += (n ** 2)
    return total


def difference_of_squares(number: int) -> int:
    total = square_of_sum(number) - sum_of_squares(number)
    return total
