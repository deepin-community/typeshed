from datetime import date, datetime, time, timedelta, tzinfo
from typing import Any, overload
from typing_extensions import Literal, TypeAlias

from babel.core import Locale
from babel.util import LOCALTZ as LOCALTZ, UTC as UTC
from pytz import BaseTzInfo

# The module contents here are organized the same way they are in the API documentation at
# http://babel.pocoo.org/en/latest/api/dates.html

# Date and Time Formatting
_Instant: TypeAlias = date | time | datetime | float | None
_PredefinedTimeFormat: TypeAlias = Literal["full", "long", "medium", "short"]

def format_datetime(
    datetime: _Instant = ..., format: _PredefinedTimeFormat | str = ..., tzinfo: tzinfo | None = ..., locale: str | Locale = ...
) -> str: ...
def format_date(
    date: date | datetime | None = ..., format: _PredefinedTimeFormat | str = ..., locale: str | Locale = ...
) -> str: ...
def format_time(
    time: time | datetime | float | None = ...,
    format: _PredefinedTimeFormat | str = ...,
    tzinfo: tzinfo | None = ...,
    locale: str | Locale = ...,
) -> str: ...
def format_timedelta(
    delta: timedelta | int,
    granularity: Literal["year", "month", "week", "day", "hour", "minute", "second"] = ...,
    threshold: float = ...,
    add_direction: bool = ...,
    format: Literal["narrow", "short", "medium", "long"] = ...,
    locale: str | Locale = ...,
) -> str: ...
def format_skeleton(
    skeleton: str, datetime: _Instant = ..., tzinfo: tzinfo | None = ..., fuzzy: bool = ..., locale: str | Locale = ...
) -> str: ...
def format_interval(
    start: _Instant,
    end: _Instant,
    skeleton: str | None = ...,
    tzinfo: tzinfo | None = ...,
    fuzzy: bool = ...,
    locale: str | Locale = ...,
) -> str: ...

# Timezone Functionality
@overload
def get_timezone(zone: str | BaseTzInfo | None = ...) -> BaseTzInfo: ...
@overload
def get_timezone(zone: tzinfo) -> tzinfo: ...
def get_timezone_gmt(
    datetime: _Instant = ...,
    width: Literal["long", "short", "iso8601", "iso8601_short"] = ...,
    locale: str | Locale = ...,
    return_z: bool = ...,
) -> str: ...

_DtOrTzinfo: TypeAlias = datetime | tzinfo | str | int | time | None

def get_timezone_location(dt_or_tzinfo: _DtOrTzinfo = ..., locale: str | Locale = ..., return_city: bool = ...) -> str: ...
def get_timezone_name(
    dt_or_tzinfo: _DtOrTzinfo = ...,
    width: Literal["long", "short"] = ...,
    uncommon: bool = ...,
    locale: str | Locale = ...,
    zone_variant: Literal["generic", "daylight", "standard"] | None = ...,
    return_zone: bool = ...,
) -> str: ...

# Note: While Babel accepts any tzinfo for the most part, the get_next_timeout_transition()
# function requires a tzinfo that is produced by get_timezone()/pytz AND has DST info.
# The typing here will help you with the first requirement, but will not protect against
# pytz tzinfo's without DST info, like what you get from get_timezone("UTC") for instance.
def get_next_timezone_transition(zone: BaseTzInfo | None = ..., dt: _Instant = ...) -> TimezoneTransition: ...

class TimezoneTransition:
    # This class itself is not included in the documentation, yet it is mentioned by name.
    # See https://github.com/python-babel/babel/issues/823
    activates: datetime
    from_tzinfo: tzinfo
    to_tzinfo: tzinfo
    reference_date: datetime | None
    def __init__(
        self, activates: datetime, from_tzinfo: tzinfo, to_tzinfo: tzinfo, reference_date: datetime | None = ...
    ) -> None: ...
    @property
    def from_tz(self) -> str: ...
    @property
    def to_tz(self) -> str: ...
    @property
    def from_offset(self) -> int: ...
    @property
    def to_offset(self) -> int: ...

# Data Access
def get_period_names(width: str = ..., context: str = ..., locale=...): ...
def get_day_names(width: str = ..., context: str = ..., locale=...): ...
def get_month_names(width: str = ..., context: str = ..., locale=...): ...
def get_quarter_names(width: str = ..., context: str = ..., locale=...): ...
def get_era_names(width: str = ..., locale=...): ...
def get_date_format(format: str = ..., locale=...): ...
def get_datetime_format(format: str = ..., locale=...): ...
def get_time_format(format: str = ..., locale=...): ...

# Basic Parsing
def parse_date(string, locale=..., format: str = ...): ...
def parse_time(string, locale=..., format: str = ...): ...
def parse_pattern(pattern): ...

# Undocumented
NO_INHERITANCE_MARKER: str
LC_TIME: Any
date_ = date
datetime_ = datetime
time_ = time

TIMEDELTA_UNITS: Any

def get_period_id(time, tzinfo: Any | None = ..., type: Any | None = ..., locale=...): ...

class DateTimePattern:
    pattern: Any
    format: Any
    def __init__(self, pattern, format) -> None: ...
    def __mod__(self, other): ...
    def apply(self, datetime, locale): ...

class DateTimeFormat:
    value: Any
    locale: Any
    def __init__(self, value, locale) -> None: ...
    def __getitem__(self, name): ...
    def extract(self, char): ...
    def format_era(self, char, num): ...
    def format_year(self, char, num): ...
    def format_quarter(self, char, num): ...
    def format_month(self, char, num): ...
    def format_week(self, char, num): ...
    def format_weekday(self, char: str = ..., num: int = ...): ...
    def format_day_of_year(self, num): ...
    def format_day_of_week_in_month(self): ...
    def format_period(self, char, num): ...
    def format_frac_seconds(self, num): ...
    def format_milliseconds_in_day(self, num): ...
    def format_timezone(self, char, num): ...
    def format(self, value, length): ...
    def get_day_of_year(self, date: Any | None = ...): ...
    def get_week_number(self, day_of_period, day_of_week: Any | None = ...): ...

PATTERN_CHARS: Any
PATTERN_CHAR_ORDER: str

def tokenize_pattern(pattern): ...
def untokenize_pattern(tokens): ...
def split_interval_pattern(pattern): ...
def match_skeleton(skeleton, options, allow_different_fields: bool = ...): ...
