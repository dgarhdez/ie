"""
The script should print the following:
* i
* the current working directory
* the variable `__name__`
"""

import os
from datetime import datetime

print(datetime.now())
print(os.getcwd())
print(__name__)
