#!/usr/bin/env python
# encoding: utf-8

import pytz
import dateutil.parser
import calendar as cal
import datetime


def iso_time_to_utc_timestamp(iso_time_str):

    SHANGHAI = pytz.timezone('Asia/Shanghai')

    _when = dateutil.parser.parse(iso_time_str)

    if not _when.tzname():
            _when = SHANGHAI.localize(_when)

    return cal.timegm(_when.utctimetuple())


def get_yesterday_begin_timestamp():

    SHANGHAI = pytz.timezone('Asia/Shanghai')

    today_date = datetime.datetime.now(SHANGHAI).replace(hour=0, minute=0, second=0)

    yesterday_date = today_date - datetime.timedelta(days=1)

    return cal.timegm(yesterday_date.utctimetuple())
