import subprocess
import setuptools
from setuptools.dist import Distribution
from wheel.bdist_wheel import bdist_wheel

"""
Declare binary wheels as 'non-pure'.

This forces all package tags to be set. But our package is only
non-pure because of the dynamically loaded fortran library,
which is compiled seperately, and thus depends on the platform.
The package does not depend on any specific version of CPython.

Thus we remove the abi tag, and set the python tag to the major
version of python being used (i.e. py3)
"""
class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

class custom_bdist_wheel(bdist_wheel):
    def get_tag(self):
        python, abi, plat = bdist_wheel.get_tag(self)
        # We don't use CPython
        python, abi, plat = self.python_tag, 'none', self.plat_name
        return python, abi, plat

    def run(self):
        """
        Build the fortran library first, then do regular run()
        """
        subprocess.call(['make', 'clean'], cwd='../')
        subprocess.call(['make', 'lib'], cwd='../')
        subprocess.call(['cp', '../bin/libdave.so', './src/libs/.'])
        bdist_wheel.run(self)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name             = "pydave",
    version          = "0.0.7",
    author           = "David Liptai",
    author_email     = "dliptai@swin.edu.au",
    description      = "A python wrapper for the 'dave' library",
    long_description = long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages     = ["pydave"],
    package_dir  = {"pydave" : "src"},
    package_data={"pydave": ["libs/*.so*", "libs/*.dylib*"]},
    include_package_data = True,
    classifiers  = ["Programming Language :: Python :: 3",],
    python_requires='>=3.6',
    cmdclass={'bdist_wheel': custom_bdist_wheel},
    distclass=BinaryDistribution
)
