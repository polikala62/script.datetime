'''
Created on Jun 28, 2024

@author: Karl
'''
import datetime

def strf_timedelta(in_timedelta, report_days=True, report_seconds=True):
    
    timdedelta_seconds = in_timedelta.total_seconds()
    
    minutes, seconds = [int(round(i, 0)) for i in divmod(timdedelta_seconds, 60)]
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    if report_seconds:
        
        hms_list = [hours, minutes, seconds]
        
    elif hours + minutes == 0:
        
        hms_list = ["<1 minute"]
    
    else:
        
        hms_list = [hours, minutes]
    
    if report_days and days > 0:
        
        out_str = "{}d {}".format(days, ":".join([str(i).zfill(2) for i in hms_list]))
        
    else:
        
        out_str = ":".join([str(i).zfill(2) for i in hms_list])
    
    return out_str

def strf_timedelta2(in_timedelta, report_days=True, report_seconds=True):
    
    if in_timedelta.total_seconds() < 60 and report_seconds==False:
        
        return "<1 minute"
        print("12 days 24 hrs 35 mins")
    
foo = datetime.datetime.strptime("2024-06-28-18-30-00", "%Y-%m-%d-%H-%M-%S")
bar = datetime.datetime.strptime("2024-06-28-18-30-35-20", "%Y-%m-%d-%H-%M-%S-%f")

print(str(bar-foo))
#print(strf_timedelta2(bar-foo, True, False))