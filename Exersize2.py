import random


def get_numbers_ticket(min_value, max_value, quantity):
    if min_value >= 1 and max_value <= 1000 and quantity >= 0:
        if quantity > (max_value - min_value + 1):
            return []
        result = random.sample(range(min_value, max_value + 1), quantity)
        result.sort()
    else:
        return "Внесен не верный диапазон или кол-во раз."
    return result


# int_min = int(input("Внеси минимальное кол-во числа: "))
# int_max = int(input("Внеси максимальное кол-во числа: "))
# int_quantity = int(input("Внеси кол-во чисел которые хочешь получить: "))


lottery_numbers = get_numbers_ticket(10, 15, 19)
print("Ваші лотерейні числа:", lottery_numbers)
