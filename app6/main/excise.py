from datetime import date, time, datetime, timedelta

d0 = date(year=2020, month=11, day=24)
d1 = date.fromisoformat("2020-11-24")
d2 = date.today()

[d0.year, d0.month, d0.day]
[d0.isoformat(), d0.isoweekday(), d0.ctime()]

t0 = time(hour=23, minute=1, second=1)
t1 = time.fromisoformat("10:01:01")


[t0.hour, t0.minute, t0.second]
t0.isoformat()

dt0 = datetime(year=2020, month=11, day=24, hour=10, minute=1, second=1)
dt1 = datetime.fromisoformat("2020-11-24T10:01:01")
dt2 = datetime.now()
dt3 = datetime.utcnow()

[dt0.year, dt0.month, dt0.day, dt0.hour, dt0.minute, dt0.second]
[dt0.isoformat(), dt0.isoweekday(), dt0.ctime()]

td0 =timedelta(days=1)
td1 = d2-d1
td2 = dt2 - dt1

[td2.days, td2.seconds]
[d0+td2, dt0+td2]
































