# -*- coding: utf-8 -*-
"""
Lib conversion time

@author: josélia Pires
"""

CONVERSION_TIME = 60
SECONDS_CONVERSION = 3600

def hours_to_minutes(hour):
    return  float(hour * CONVERSION_TIME)

def hours_to_seconds(hour):
    return float(hour * SECONDS_CONVERSION)

def minutes_to_seconds(minute):
    return float(minute * CONVERSION_TIME)

def seconds_to_minutes(second):
    return float(second / CONVERSION_TIME)

def seconds_to_hours(second):
    return float(second / SECONDS_CONVERSION)

