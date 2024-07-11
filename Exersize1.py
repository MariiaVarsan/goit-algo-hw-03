from datetime import datetime


def string_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except Exception as e:
        return f"Error: {e}"


def get_days_from_today(input_date_string) -> int:
    today = datetime.now().date()
    date_datetime = string_to_date(input_date_string)

    difference = today - date_datetime

    return difference.days


date_string = input("Внеси дату (в формате ГГГГ-ММ-ДД): ")

days_difference = get_days_from_today(date_string)

print(f"Різниця між поточною датою та введеною датою: {days_difference} днів")
