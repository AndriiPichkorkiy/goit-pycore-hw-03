from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    # pattern is used to convert user birthday to date
    birthday_pattern = "%Y.%m.%d"

    # list of mathed birthdays to return
    res = []

    # get today's day
    today = datetime.today().date()

    # next line for test only. Uncomment the line to test birthdays with next year
    # today = today.replace(month=12, day=31)

    # find users with nearest birthday 
    for user in users:
        # get user's birthday as class date
        birthday = datetime.strptime(user["birthday"], birthday_pattern).date()

        # set currnet year to compare the dates
        birthday_this_year = birthday.replace(year = today.year)

        # if next birthday in the next year, add 1 year
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year = today.year + 1)

        #  get difference between today and next birhday years
        next_birthday_in_days = (birthday_this_year - today).days

        #  find and add to result only birthdays in next 7 days
        if(next_birthday_in_days < 7):
            weekday = birthday_this_year.weekday()

            # if the birthday falls on a weekend, the date of the greeting is moved to the following Monday.
            if(weekday == 5 or weekday == 6):
                birthday_this_year += timedelta(days= 7 - weekday)
            
            res.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime(birthday_pattern)})

    return res

users = [
    {"name": "John Doe", "birthday": "1985.01.03"},
    {"name": "Jane Smith", "birthday": "1990.07.12"},
    {"name": "Jane Doe", "birthday": "1990.07.07"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)