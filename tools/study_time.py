def strptime(time_str):
    h, m, s = [int(time) for time in time_str.split(":")]
    return h * 3600 + m * 60 + s

def timepstr(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return f'{h:0>2}:{m:0>2}:{s:0>2}'

