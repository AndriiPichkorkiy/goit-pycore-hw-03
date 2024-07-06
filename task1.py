from datetime import datetime
import re

def get_days_from_today(date: str) -> int:
    # validetion for string
    if type(date) != str:
        return "Custom error: input value is not a string"
    
    # validetion for date
    # valid pattern is: YYYY-MM-DD
    if not re.match(r"^\d{4}-[0|1]\d-[0-3]\d$", date):
        return "Custom error: input value  is not valid"

    # get today's day
    today = datetime.today()

    # convert input value to class datetime
    input_date = datetime.strptime(date, "%Y-%m-%d")

    # calculate differense
    time_delta = today - input_date

    # return only days
    return time_delta.days

# crash tests
print(get_days_from_today(324324234324324324324))
print(get_days_from_today("Check this date: 2020-10-09"))
print(get_days_from_today("2020-10-09 Check this date"))
print(get_days_from_today("10-09-2020"))
print(get_days_from_today('2020-99-99'))

# test positive 
print(get_days_from_today('2020-10-09'))

# test negative
print(get_days_from_today('9999-12-31'))