
import random

def get_numbers_ticket(min_value, max_value, quantity):
    if min_value >= 1 and max_value <= 1000 and quantity >= 0:
        result = []
        for _ in range(quantity):
            result = random.sample(range(min_value, max_value + 1), quantity)
            result.sort()
    else:
        result = print("Внесен не верный диапазон или кол-во раз.")

    return result

# int_min = int(input("Внеси минимальное кол-во числа: "))
# int_max = int(input("Внеси максимальное кол-во числа: "))
# int_quantity = int(input("Внеси кол-во чисел которые хочешь получить: "))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
