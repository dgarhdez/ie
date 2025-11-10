# if executed print the current date and time and "Executed from the command line"
# if imported print the current date and time and "Imported from {filename}"

import datetime
import os


def print_current_date_and_time():
    print(datetime.datetime.now())


def print_current_working_directory():
    print(os.getcwd())


def print_name():
    print(__name__)


if __name__ == "__main__":  # executing
    print_current_date_and_time()
    print("Executed from the command line")
else:  # import
    print_current_date_and_time()
    print(f"Imported from {__name__}")
