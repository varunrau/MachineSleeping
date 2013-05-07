import datetime as dt

def inBedByHour(start_date, h):
    return start_date.time() < dt.time(hour=h)

def ninetyMinuteCycle(seconds):
    ninetyMinutes = 90 * 60
    val = ninetyMinutes % seconds
    margin = 5 * 60 # 15 seconds
    return val < margin or margin + val > ninetyMinutes

def getTime(start_time, end_time):
    start_date = dt.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_date = dt.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    time_delta = end_date - start_date
    seconds = time_delta.total_seconds()
    return (start_date, end_date, seconds)
