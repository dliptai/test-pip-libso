import setuptools
from setuptools.dist import Distribution
import subprocess

subprocess.call(['make', 'clean'], cwd='../dave')
subprocess.call(['make', 'lib'], cwd='../dave')
subprocess.call(['cp', '../dave/libdave.so', 'pydave/libs/.'])

with open("README.md", "r") as fh:
    long_description = fh.read()


# from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

# class bdist_wheel(_bdist_wheel):

#     def finalize_options(self):
#         _bdist_wheel.finalize_options(self)
#         # Mark us as not a pure python package
#         self.root_is_pure = False

#     # def get_tag(self):
#     #     python, abi, plat = _bdist_wheel.get_tag(self)
#     #     # We don't contain any python source
#     #     python, abi = 'py2.py3', 'none'
#     #     return python, abi, plat


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""

    def has_ext_modules(self):
        return True

    # def is_pure(self):
    #     return False

    # def has_c_libraries(self):
    #     return True

setuptools.setup(
    name             = "pydave",
    version          = "0.0.6",
    author           = "David Liptai",
    author_email     = "dliptai@swin.edu.au",
    description      = "A python wrapper for the 'dave' library",
    long_description = long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages     = ["pydave"],
    package_data = {"pydave" : ["libs/*.so*"]},
    classifiers  = [
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    distclass=BinaryDistribution,
    # cmdclass={'bdist_wheel': bdist_wheel},
)
