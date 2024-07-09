from datetime import datetime
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date_string) -> int:
    today = datetime.now().date()
    date_datetime = string_to_date(date_string)

    difference = today - date_datetime

    return difference.days

date_string = input("Внеси дату (в формате ГГГГ-ММ-ДД): ")

days_difference = get_days_from_today(date_string)

print(f"Різниця між поточною датою та введеною датою: {days_difference} днів")