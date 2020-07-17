import subprocess
import setuptools
from setuptools.dist import Distribution
from wheel.bdist_wheel import bdist_wheel

"""
Build the fortran library first, then do regular run()
"""
class custom_bdist_wheel(bdist_wheel):
    def run(self):
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
)
