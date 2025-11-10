# The script should print the current date and time,
# and the current working directory.

import datetime
import os

def print_current_date_and_time():
    print(datetime.datetime.now())

def print_current_working_directory():
    print(os.getcwd())

def print_name():
    print(__name__)

print_current_date_and_time()
print_current_working_directory()
print_name()