from datetime import datetime

def time_delta(t1: str, t2: str) -> int:
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    return abs(int((dt1 - dt2).total_seconds()))