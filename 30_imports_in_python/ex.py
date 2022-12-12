from mymodule import divide

print(divide(10, 2))

# -- __name__ --

print(__name__)

# -- importing with names --

import mymodule

print('code.py:', __name__)

import sys
print(sys.path)
