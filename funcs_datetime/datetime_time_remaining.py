'''
Created on Jun 20, 2024

@author: Karl
'''

import datetime, numpy

def datetime_time_remaining(pr_timedelta_list, pr_time, pr_count, pr_total, timedelta_span=0, method="SIMPLE"):
    
    # Add timedelta to list.
    pr_timedelta_list.append(pr_time.total_seconds())
    
    # If timedelta window is zero, set it to the length of the list.
    if timedelta_span == 0:
        
        timedelta_span = len(pr_timedelta_list)
        
    # Clip timedelta list to length of window.
    clip_pr_timedelta_list = pr_timedelta_list[0:timedelta_span]
    
    # Get the number of iterations remaining.
    pr_remaining = pr_total - pr_count
    
    if method == "SIMPLE":
        
        # Get the average amount of time elapsed per iteration within the timedelta window.
        pr_avg_time = numpy.average(clip_pr_timedelta_list)
        
    elif method == "WEIGHTED":
        
        # Weight more recent iterations higher.
        pr_avg_time = numpy.average(clip_pr_timedelta_list, weights=range(0,len(clip_pr_timedelta_list)))
    
    else:
        
        raise Exception('Method must be "SIMPLE" or "WEIGHTED"')
    
    # Multiply average time by remaining runs to estimate the amount of time remaining.
    est_runtime_delta = datetime.timedelta(seconds=(pr_remaining * pr_avg_time))
    
    # 
    return est_runtime_delta