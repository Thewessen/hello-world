import re
from datetime import date
from calendar import day_name, monthcalendar
from itertools import islice


class MeetupDayException(Exception):
    def __init__(self, *args):
        super(Exception, self).__init__(*args)


def meetup(year: int, month: int, week: str, day_of_week: str) -> object:
    """Calculate the date of meetups."""
    day_int = list(day_name).index(day_of_week)
    days = (w[day_int] for w in monthcalendar(year, month) if w[day_int])
    if week == 'teenth':
        return date(year, month, next(day for day in days if day >= 13))
    if week == 'last':
        return date(year, month, max(days))
    th = int(re.match(r'^\d+', week).group(0))
    try:
        return date(year, month, next(islice(days, th - 1, None)))
    except StopIteration:
        raise MeetupDayException('No Valid meetupday')
