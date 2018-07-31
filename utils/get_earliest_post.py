# Find the pid of the earliest valid post


import functools
import requests


@functools.lru_cache(maxsize=None) # Cache results for better performance
def check_pid_exist(pid):
    # Must use IPv4 when connecting to the server. Something wrong with its IPv6 server.
    # When using requests, the URL resolution is IPv6 by default (I have no idea why). Being a high level package, there are no way to config the IP protocol version. So we have to use the IP directly when connecting.
    headers = {'Host': 'www.pkuhelper.com'} # MUST add this!
    ans = requests.get("http://162.105.205.61/services/pkuhole/api.php?action=getcomment&pid=" + str(pid), headers=headers)
    ans = ans.json()
    
    # Determining whether the post exsits. If doesn't, code would be 1.
    try:
        if ans["code"] == 0:
            print("True for ", pid)
            return True
        elif ans["code"] == 1:
            print("False for ", pid)
            return False
    except:
        print("Something Wrong")
        return False
        
def bisection_search(start_param, end_param, func):
    if start_param + 1 == end_param:
        return end_param

    start_value =  func(start_param) 
    print("For ", start_param, ", answer is", start_value) 
    end_value   =  func(end_param)
    print("For ", end_param, ", answer is", end_value)
    
    assert(isinstance(start_value, bool))
    assert(isinstance(end_value, bool))
    assert(start_value != end_value)
    
    middle_param = (start_param + end_param) // 2
    middle_value = func(middle_param)
    assert(isinstance(middle_value, bool))
    if middle_value == start_value:
        return bisection_search(middle_param, end_param, func)
    elif middle_value == end_value:
        return bisection_search(start_param,  middle_param, func)


if __name__ == "__main__":
    a = bisection_search(100, 50000, check_pid_exist)
    print("First valid post is ", a)
else:
    print("Stand alone program, not to be imported!")





