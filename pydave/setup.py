import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            # Mark us as not a pure python package
            self.root_is_pure = False

        # def get_tag(self):
        #     python, abi, plat = _bdist_wheel.get_tag(self)
        #     # We don't contain any python source
        #     python, abi = 'py2.py3', 'none'
        #     return python, abi, plat

except ImportError:
    bdist_wheel = None

setuptools.setup(
    name             = "pydave",
    version          = "0.0.1",
    author           = "David Liptai",
    author_email     = "dliptai@swin.edu.au",
    description      = "A python wrapper for the 'dave' library",
    long_description = long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages     = ["pydave"],
    package_data = {"pydave" : ["libs/*.so"]},
    classifiers  = [
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    cmdclass={'bdist_wheel': bdist_wheel},
)
