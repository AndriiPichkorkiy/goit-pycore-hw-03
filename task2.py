import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    # type validation
    if type(min) != int or type(max) != int or type(quantity) != int:
        return []
    
    # count validations
    if 1 > min or min > 1000:
        return []
    if 1 > max or max > 1000:
        return []
    if max - min < quantity:
        return []
    
    # generate random tickets in range min/max
    tickets = random.sample(range(min, max), quantity)

    # sort in order of greater number
    tickets.sort()

    return tickets

# crash tests
crash_1 = get_numbers_ticket(0, 49, 6)
print("Ваші лотерейні числа:", crash_1)

crash_2 = get_numbers_ticket(1, 1001, 6)
print("Ваші лотерейні числа:", crash_2)

crash_3 = get_numbers_ticket(950, 1000, 51)
print("Ваші лотерейні числа:", crash_3)

crash_4 = get_numbers_ticket("John", "Doe", 51)
print("Ваші лотерейні числа:", crash_4)

# valid tests
valid_1 = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", valid_1)

valid_2 = get_numbers_ticket(1, 1000, 15)
print("Ваші лотерейні числа:", valid_2)

valid_3 = get_numbers_ticket(950, 1000, 3)
print("Ваші лотерейні числа:", valid_3)

