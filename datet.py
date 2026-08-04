import datetime

print(dir(datetime))

[
    "MAXYEAR",
    "MINYEAR",
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__spec__",
    "date",
    "datetime",
    "datetime_CAPI",
    "sys",
    "time",
    "timedelta",
    "timezone",
    "tzinfo",
]


from datetime import datetime

now = datetime.now()
print(now)  # 2026-08-04 11:00:01.581984
day = now.day  # 4
month = now.month  # 8
year = now.year  # 2026
hour = now.hour  # 11
minute = now.minute  # 0
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")  # 4/8/2026, 11:0

# ! this file was originally named "datetime.py" which caused an AtributeError that caused circular import and to fix it, the file was renamed to "datet.py"
# * keep in mind for future reference
