import subprocess
import setuptools
from setuptools.command.install import install
from wheel.bdist_wheel import bdist_wheel
import inspect

def build(src_dir='../'):
    print("\n>>> Building fortran source in directory: ",src_dir, flush=True)
    subprocess.call(['make', 'clean'], cwd=src_dir)
    subprocess.call(['make', 'lib'], cwd=src_dir)
    subprocess.call(['cp', src_dir+'bin/libdave.so', './src/libs/.'])
    print("<<< Finished building fortran source.\n", flush=True)

"""
Build the fortran library first, then do regular run()
"""
class custom_bdist_wheel(bdist_wheel):
     def run(self):
        build()
        bdist_wheel.run(self)

class custom_install(install):
    def run(self):
        # Don't recompile if bdist_wheels was already run
        if self._called_from_setup(inspect.currentframe()): build()
        install.run(self)

with open("README.md", "r") as fh:
    long_description = fh.read()

print('\n>>>>> running setup.py >>>>>', flush=True)
setuptools.setup(
    name             = "pydave",
    version          = "0.0.8-1",
    author           = "David Liptai",
    author_email     = "dliptai@swin.edu.au",
    description      = "A python wrapper for the 'dave' library",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dliptai/test-pip-libso",
    packages     = ["pydave"],
    package_dir  = {"pydave" : "src"},
    package_data={"pydave": ["libs/*.so*", "libs/*.dylib*"]},
    include_package_data = True,
    classifiers  = ["Programming Language :: Python :: 3",],
    python_requires='>=3.6',
    cmdclass={
        'install': custom_install,
        'bdist_wheel': custom_bdist_wheel
        },
)
print('<<<<< end running setup.py <<<<<\n', flush=True)
