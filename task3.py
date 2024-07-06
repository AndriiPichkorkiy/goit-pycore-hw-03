import re

def normalize_phone(phone_number: str) -> str:
    # pattern to remove extra symbols
    pattern = r"[^\d|\+]"

    # remove extra symbols
    phone_number = re.sub(pattern, "", phone_number)

    # normalize number by adding +38 to completely fill in the country code
    if phone_number.startswith("0"):
        phone_number = "+38" + phone_number
    # normalize number by adding plus to the country code
    elif phone_number.startswith("38"):
        phone_number = "+" + phone_number

    return phone_number
     

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)