import datetime

def get_birthdays_per_week(users):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    current_day = datetime.datetime.now().date()
    next_week = current_day + datetime.timedelta(days=7)

    print("Ближчі дні народження:")

    for day in range(8):
        target_day = current_day + datetime.timedelta(days=day)
        day_name = days_of_week[target_day.weekday()]
        birthday_people = [user["name"] for user in users if user["birthday"].month == target_day.month and user["birthday"].day == target_day.day]

        if birthday_people:
            if day_name == "Sunday":
                print("Monday:", ", ".join(birthday_people))
            elif day_name == "Saturday":
                print("Monday:", ", ".join(birthday_people))
            else:
                print(f"{day_name}:", ", ".join(birthday_people))

users = []

get_birthdays_per_week(users)
