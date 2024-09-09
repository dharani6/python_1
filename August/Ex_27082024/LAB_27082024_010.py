import functools
import time

def time_decorator(func):

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Time take to execute {end_time} '-' {start_time} '='{end_time-start_time}")
    return wrapper()

@time_decorator
def test_ui_1():
    print("add the function, time take by this function")
    time.sleep(2)

'''
@staticmethod
@classmethod
@property
@ functools.wraps
used to add logs 
before 
after 
logging - add log to the autoamtion

'''
