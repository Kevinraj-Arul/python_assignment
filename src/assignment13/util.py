from datetime import datetime

def parse_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, "%a %d %b %Y %H:%M:%S %z")

def time_difference(t1_str, t2_str):
    
    t1 = parse_timestamp(t1_str)
    t2 = parse_timestamp(t2_str)
    diff = abs(int((t1 - t2).total_seconds()))
    return diff