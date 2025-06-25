def add_time(start, duration, starting_day=None):
    # Days of the week mapping
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert start time to 24-hour format
    if period.upper() == "PM" and start_hour != 12:
        start_hour += 12
    elif period.upper() == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Add minutes and handle overflow
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    # Add hours and calculate total days passed
    total_hours = start_hour + dur_hour + extra_hour
    days_passed = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_period = "PM"

    # Format time
    new_time = f"{final_hour}:{final_minute:02d} {final_period}"

    # Handle optional day
    if starting_day:
        index = days_of_week.index(starting_day.capitalize())
        new_index = (index + days_passed) % 7
        new_day = days_of_week[new_index]
        new_time += f", {new_day}"

    # Add suffix for days passed
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time

# add_time('9:45', '64:10', 'wednesday')
add_time('11:43 PM', '24:20', 'tueSday')