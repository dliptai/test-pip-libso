import re
import json
import sys
import subprocess
import os

# """
# Require std.input to be piped. Then load as string.
# """
if sys.stdin.isatty():
    raise Exception("No data was piped to program")
else:
  text = sys.stdin.read()
  print(text)

# """
# Remove newline characters except lines begining with... (see below)
# """
text = text.replace('\n', ' ')
text = text.replace('In order to achieve the tag platform tag',
                    '\nIn order to achieve the tag platform tag')


# """
# Extract the dictionary mapping external libraries to their paths
# """
regex_libs = re.compile(
    'The following external shared libraries are required by the wheel: (\{.*?\})')
lib_paths = regex_libs.findall(text)[0].replace('\'', '\"') # json requires double quotes
lib_paths = json.loads(lib_paths)


# """
# Extract the list of libraries required by the current manylinux platform
# """
PLAT = os.environ.get('PLAT')
expression = 'In order to achieve the tag platform tag \"%s\" the following shared library dependencies will need to be eliminated:(.*)' % PLAT
regexp     = re.compile(expression)
libs       = regexp.findall(text)[0].split(',')
libs_req   = [l.strip() for l in libs]


# """
# Copy required libraries to src/libs/
# """
for lib in libs_req:
  src  = lib_paths[lib]
  dest = os.getcwd()+'/src/libs/'+lib
  print('copying',src,'to',dest)
  subprocess.call(['cp', src, dest])
