# pyDave

This package contains the python bindings of a basic library written in fortran.

## To upload to TestPyPI
1. Copy the shared object library to `src/libs/`
2. Build the binary distribution with `python setup.py bdist_wheel`
3. To upload to TestPyPI `twine upload --repository testpypi dist/*`
4. To install somewhere `pip install --index-url https://test.pypi.org/simple/ --no-deps <package-name>`
5. To uninstall `pip uninstall <package-name>`
