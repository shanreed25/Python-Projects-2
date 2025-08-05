from datetime import date, timedelta

#TODO: Get the dates of the last two business days not including today
# use the datetime module
def get_last_two_business_days():
    today_date = date.today()
    business_days = []
    days_back = 1
    while len(business_days) < 2:
        previous_day = today_date - timedelta(days=days_back)
        # weekday() returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
        # Weekdays are 0-4
        if previous_day.weekday() < 5:  # Check if it's a weekday
            business_days.append(previous_day)
        days_back += 1
    return business_days