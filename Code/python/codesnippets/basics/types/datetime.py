# Datetime
# Module 'datetime' provides 'date' date_variable, 'time' time_variable, 'datetime' date_time_variable and 'timedelta' time_delta_variable classes. All are immutable and hashable.
# Time and datetime objects can be 'aware' <a>, meaning they have defined timezone, or 'naive' <n>, meaning they don't.
# If object is naive, it is presumed to be in the system's timezone.

from datetime import date, time, datetime, timedelta
from dateutil.tz import UTC, tzlocal, gettz, datetime_exists, resolve_imaginary

# Constructors
date_variable  = date(year, month, day)
time_variable  = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)
date_time_variable = datetime(year, month, day, hour=0, minute=0, second=0, ...)
time_delta_variable = timedelta(weeks=0, days=0, hours=0, minutes=0, seconds=0, ...)

# Use 'date_or_date_time_variable.weekday()' to get the day of the week (Mon == 0).
# 'fold=1' means the second pass in case of time jumping back for one hour.
# Timedelta normalizes arguments to ±days, seconds (< 86 400) and microseconds (< 1M).


# Now
date__or_date_time_NOW_variable  = D/DT.today()                     # Current local date or naive datetime.
date_time_NOW_variable    = DT.utcnow()                      # Naive datetime from current UTC time.
<DTa>    = DT.now(<tzinfo>)                 # Aware datetime from current tz time.
# To extract time use 'date_time_NOW_variable.time()', '<DTa>.time()' or '<DTa>.timetz()'.


# Timezone
tzinfo = UTC                              # UTC timezone. London without DST.
tzinfo = tzlocal()                        # Local timezone. Also gettz().
tzinfo = gettz('<Continent>/<City>')      # 'Continent/City_Name' timezone or None.
<DTa>    = date_time_variable.astimezone(<tzinfo>)        # Datetime, converted to the passed timezone.
<Ta/DTa> = <T/DT>.replace(tzinfo=<tzinfo>)  # Unconverted object with a new timezone.


# Encode
date_or_time_or_date_time_variable = D/T/DT.fromisoformat('<iso>')    # Object from ISO string. Raises ValueError.
date_time_variable     = date_time_variable.strptime(<str>, '<format>')   # Datetime from str, according to format.
date__or_date_time_NOW_variable  = date__or_date_time_NOW_variable.fromordinal(<int>)          # D/DTn from days since the Gregorian NYE 1.
date_time_NOW_variable    = date_time_variable.fromtimestamp(<real>)         # Local time DTn from seconds since the Epoch.
<DTa>    = DT.fromtimestamp(<real>, <tz.>)  # Aware datetime from seconds since the Epoch.

# ISO strings come in following forms: 'YYYY-MM-DD', 'HH:MM:SS.ffffff[±<offset>]', or both separated by an arbitrary character. Offset is formatted as: 'HH:MM'.
# Python uses the Unix Epoch: '1970-01-01 00:00 UTC', '1970-01-01 01:00 CET', ...

# Decode
<str>    = date_or_time_or_date_time_variable.isoformat(sep='T')      # Also timespec='auto/hours/minutes/seconds'.
<str>    = date_or_time_or_date_time_variable.strftime('<format>')    # Custom string representation.
<int>    = date_or_date_time_variable.toordinal()               # Days since Gregorian NYE 1, ignoring time and tz.
<float>  = date_time_NOW_variable.timestamp()                # Seconds since the Epoch, from DTn in local tz.
<float>  = <DTa>.timestamp()                # Seconds since the Epoch, from DTa.

# Format
dt = datetime.strptime('2015-05-14 23:39:00.00 +02:00', '%Y-%m-%d %H:%M:%S.%f %z')
dt.strftime("%A, %dth of %B '%y, %I:%M%p %Z")
# OUTPUTS : "Thursday, 14th of May '15, 11:39PM UTC+02:00"
# '%Z' only accepts 'UTC/GMT' and local timezone's code. '%z' also accepts '±HHMM'.
# For abbreviated weekday and month use '%a' and '%b'.


# Arithmetics
date_or_date_time_variable   = date_or_date_time_variable  ± time_delta_variable                   # Returned datetime can fall into missing hour.
time_delta_variable     = date__or_date_time_NOW_variable - date__or_date_time_NOW_variable                # Returns the difference, ignoring time jumps.
time_delta_variable     = <DTa>   - <DTa>                  # Ignores time jumps if they share tzinfo object.
time_delta_variable     = time_delta_variable  * <real>                 # Also: time_delta_variable = abs(time_delta_variable) and time_delta_variable = time_delta_variable ±% time_delta_variable
float_dates_calc  = time_delta_variable    / time_delta_variable                   # How many weeks/years there are in TD. Also '//'.

