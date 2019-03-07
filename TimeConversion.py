#!/bin/python3

import os
import sys

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

# Function Description
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# timeConversion has the following parameter(s):
# s: a string representing time in 12 hour format       hh:mm:ssAM or hh:mm:ssPM   where 01 <= hh <= 12 and 00 <= mm, ss, <= 59
#
# Complete the timeConversion function below.
#
#Sample input
#07:05:45PM       = 19:05:45

def timeConversion(s):
    #
    # Write your code here.
    #
    s.split(":")
    hours = int(s[0:2])
    convTime = ""
    if 'P' in s:
        if hours == 12:
            convTime += s[:8]
        else:    
            hours += 12
            convTime += str(hours)
            convTime += s[2:8]
    else:
        if hours == 12:
            convTime += '00'
            convTime += s[2:8]
        else:
            convTime += s[:8]

    return convTime

if __name__ == '__main__':
    
    print("Enter a time in HH:MM:SSAM or HH:MM:SSPM format to convert. ")
    s = input()

    result = timeConversion(s)
    print(result)
