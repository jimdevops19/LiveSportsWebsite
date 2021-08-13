import datetime


def get_ft_time(starting_time_str):
    now = datetime.datetime.now().timestamp()
    starting_time_obj = datetime.datetime.now().replace(
        hour=int(starting_time_str.split(':')[0]),
        minute=int(starting_time_str.split(':')[1]),
        second=0,
        microsecond=0,
    )
    delta = now - starting_time_obj.timestamp()

    return format_time(float(delta))

def format_time(total_seconds):
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds - (60 * minutes))

    if minutes > 0:
        return f"{minutes:02}:{seconds:02}"
    else:
        return "00:00"
