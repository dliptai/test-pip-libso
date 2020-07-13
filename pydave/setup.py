import subprocess
import setuptools
from setuptools.dist import Distribution
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

"""
Build the fortran library
"""
subprocess.call(['make', 'clean'], cwd='../dave')
subprocess.call(['make', 'lib'], cwd='../dave')
subprocess.call(['cp', '../dave/libdave.so', 'src/libs/.'])

"""
Declare binary wheels as 'non-pure'.

This forces all package tags to be set. But our package is only
non-pure because of the dynamically loaded fortran library,
which is compiled seperately, and thus depends on the platform.
The package does not depend on any specific version of CPython.

Thus we remove the abi tag, and set the python tag to the major
version of python being used (i.e. py3)
"""
class bdist_wheel(_bdist_wheel):

    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        # Mark us as not a pure python package
        self.root_is_pure = False

    def get_tag(self):
        python, abi, plat = _bdist_wheel.get_tag(self)
        # We don't use CPython
        python, abi = self.python_tag, 'none'
        return python, abi, plat

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name             = "pydave",
    version          = "0.0.7   ",
    author           = "David Liptai",
    author_email     = "dliptai@swin.edu.au",
    description      = "A python wrapper for the 'dave' library",
    long_description = long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages     = ["pydave"],
    package_dir  = {"pydave" : "src"},
    package_data = {"pydave" : ["libs/*.so*"]},
    classifiers  = ["Programming Language :: Python :: 3",],
    python_requires='>=3.6',
    cmdclass={'bdist_wheel': bdist_wheel},
)
