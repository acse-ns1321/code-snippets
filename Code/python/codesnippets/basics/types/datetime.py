# Datetime
# Module 'datetime' provides 'date' <D>, 'time' <T>, 'datetime' <DT> and 'timedelta' <TD> classes. All are immutable and hashable.
# Time and datetime objects can be 'aware' <a>, meaning they have defined timezone, or 'naive' <n>, meaning they don't.
# If object is naive, it is presumed to be in the system's timezone.

from datetime import date, time, datetime, timedelta
from dateutil.tz import UTC, tzlocal, gettz, datetime_exists, resolve_imaginary

# Constructors
<D>  = date(year, month, day)
<T>  = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)
<DT> = datetime(year, month, day, hour=0, minute=0, second=0, ...)
<TD> = timedelta(weeks=0, days=0, hours=0, minutes=0, seconds=0, ...)

# Use '<D/DT>.weekday()' to get the day of the week (Mon == 0).
# 'fold=1' means the second pass in case of time jumping back for one hour.
# Timedelta normalizes arguments to ±days, seconds (< 86 400) and microseconds (< 1M).


# Now
<D/DTn>  = D/DT.today()                     # Current local date or naive datetime.
<DTn>    = DT.utcnow()                      # Naive datetime from current UTC time.
<DTa>    = DT.now(<tzinfo>)                 # Aware datetime from current tz time.
# To extract time use '<DTn>.time()', '<DTa>.time()' or '<DTa>.timetz()'.


# Timezone
<tzinfo> = UTC                              # UTC timezone. London without DST.
<tzinfo> = tzlocal()                        # Local timezone. Also gettz().
<tzinfo> = gettz('<Continent>/<City>')      # 'Continent/City_Name' timezone or None.
<DTa>    = <DT>.astimezone(<tzinfo>)        # Datetime, converted to the passed timezone.
<Ta/DTa> = <T/DT>.replace(tzinfo=<tzinfo>)  # Unconverted object with a new timezone.


# Encode
<D/T/DT> = D/T/DT.fromisoformat('<iso>')    # Object from ISO string. Raises ValueError.
<DT>     = DT.strptime(<str>, '<format>')   # Datetime from str, according to format.
<D/DTn>  = D/DT.fromordinal(<int>)          # D/DTn from days since the Gregorian NYE 1.
<DTn>    = DT.fromtimestamp(<real>)         # Local time DTn from seconds since the Epoch.
<DTa>    = DT.fromtimestamp(<real>, <tz.>)  # Aware datetime from seconds since the Epoch.

# ISO strings come in following forms: 'YYYY-MM-DD', 'HH:MM:SS.ffffff[±<offset>]', or both separated by an arbitrary character. Offset is formatted as: 'HH:MM'.
# Python uses the Unix Epoch: '1970-01-01 00:00 UTC', '1970-01-01 01:00 CET', ...

# Decode
<str>    = <D/T/DT>.isoformat(sep='T')      # Also timespec='auto/hours/minutes/seconds'.
<str>    = <D/T/DT>.strftime('<format>')    # Custom string representation.
<int>    = <D/DT>.toordinal()               # Days since Gregorian NYE 1, ignoring time and tz.
<float>  = <DTn>.timestamp()                # Seconds since the Epoch, from DTn in local tz.
<float>  = <DTa>.timestamp()                # Seconds since the Epoch, from DTa.

# Format
>>> dt = datetime.strptime('2015-05-14 23:39:00.00 +02:00', '%Y-%m-%d %H:%M:%S.%f %z')
>>> dt.strftime("%A, %dth of %B '%y, %I:%M%p %Z")
# "Thursday, 14th of May '15, 11:39PM UTC+02:00"
# '%Z' only accepts 'UTC/GMT' and local timezone's code. '%z' also accepts '±HHMM'.
# For abbreviated weekday and month use '%a' and '%b'.


# Arithmetics
<D/DT>   = <D/DT>  ± <TD>                   # Returned datetime can fall into missing hour.
<TD>     = <D/DTn> - <D/DTn>                # Returns the difference, ignoring time jumps.
<TD>     = <DTa>   - <DTa>                  # Ignores time jumps if they share tzinfo object.
<TD>     = <TD>    * <real>                 # Also: <TD> = abs(<TD>) and <TD> = <TD> ±% <TD>
<float>  = <TD>    / <TD>                   # How many weeks/years there are in TD. Also '//'.