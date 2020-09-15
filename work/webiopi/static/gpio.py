import webiopi
import sys
import os

sd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(sd)

import test_python

@webiopi.macro
def run_script(data):
    if data == "0":
        result = test_python.create_file(sd)
        return str(result)
    else:
        return 'error'
