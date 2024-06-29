'''
Created on Jun 29, 2024

@author: Karl
'''
import datetime

# Takes a timedelta and returns a concise string estimating the amount of time.
def timedelta_to_estimate(in_timedelta):
    
    # Get total number of seconds in timedelta.
    timdedelta_seconds = in_timedelta.total_seconds()
    
    # If duration is longer than a year (365 days, what's even a leap year).
    if timdedelta_seconds >= 31536000:
        
        div_val = 31536000
        unit_str = "year" if timdedelta_seconds < (div_val*1.05) else "years"
        
    # If duration is longer than a month (30 days, everyone can share with February).
    elif timdedelta_seconds >= 2592000:
        
        div_val = 2592000
        unit_str = "month" if timdedelta_seconds < (div_val*1.05) else "months"
    
    # If duration is longer than a week.
    elif timdedelta_seconds >= 604800:
        
        div_val = 604800
        unit_str = "week" if timdedelta_seconds < (div_val*1.05) else "weeks"
    
    # If duration is longer than a day.
    elif timdedelta_seconds >= 86400:
        
        div_val = 86400
        unit_str = "day" if timdedelta_seconds < (div_val*1.05) else "days"
    
    # If duration is longer than an hour.
    elif timdedelta_seconds >= 3600:
        
        div_val = 3600
        unit_str = "hour" if timdedelta_seconds < (div_val*1.05) else "hours"
    
    # If duration is longer than a minute.
    elif timdedelta_seconds >= 60:
        
        div_val = 60
        unit_str = "minute" if timdedelta_seconds < (div_val*1.05) else "minutes"
    
    # If duration is less than a minute.
    else:
        
        # Return string.
        return "< 1 minute"
    
    # Divide the total number of seconds by the div_val, round to one decimal place, and cast to string.
    print_val = str(round(timdedelta_seconds/div_val, 1))
    
    # Remove decimal place if decimal is zero, or if script will return minutes.
    if print_val.endswith(".0") or unit_str in ["minute", "minutes"]:
        print_val = print_val[:-2]
    
    # Combine print_val and unit_str, and return.
    return "{} {}".format(print_val, unit_str)

'''
TEST
foo = datetime.datetime.strptime("2024-06-28-18-30-00", "%Y-%m-%d-%H-%M-%S")
bar = datetime.datetime.strptime("2029-11-28-18-31-32", "%Y-%m-%d-%H-%M-%S")

print(timedelta_to_estimate(bar-foo))
'''