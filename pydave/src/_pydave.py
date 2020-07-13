from ctypes import *
from pkg_resources import resource_filename

libdave = CDLL(resource_filename(__name__, 'libs/libdave.so'))

def multiply(x, y):
  c_x = c_float(x)
  c_y = c_float(y)
  c_z = c_float(x)

  libdave.dave_multiply(byref(c_x),
                        byref(c_y),
                        byref(c_z))

  return c_z.value
