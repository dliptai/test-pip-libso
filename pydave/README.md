# pyDave

This is the python version of the dave library (originally written in fortran)

## To upload to TestPyPI
1. Copy the shared object library to `libs` folder
2. Build the binary distribution with `python setup.py bdist_wheel`
3. To upload to TestPyPI `twine upload --repository testpypi dist/*`
4. To install somewhere `pip install --index-url https://test.pypi.org/simple/ --no-deps <package-name>`
5. To uninstall `pip uninstall <package-name>`
