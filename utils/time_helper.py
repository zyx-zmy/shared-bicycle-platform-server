import datetime


def dtt(time):
    return time.timestamp()


def ttd(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

