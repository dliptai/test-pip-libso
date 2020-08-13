# Python package + shared object (.so library) test
This repo is a testing ground for building a shared object library, and then including this in a python package that can be uploaded to PyPI.

Basic idea/steps:

1. Declare a Fortran subroutine with "bind c" in `libdave.f90`
2. Compile this into a shared object library (.so) using `-shared` and `-fPIC` flags
3. Copy the library into a python package
4. Load the library using CDLL from ctypes, and create a python binding for the subroutine
5. Upload the python package to TestPyPI

## Fortran to shared object library
The Fortran library is in `src/libdave.f90`. It contains a subroutine declared with `bind(c)`.

To compile this into a shared object library, type `make` or `make lib`.

### Tests
To test that the function is callable from the library in Fortran type
```
make ftest
./build/ftest
```

Similarly to test that it's callable in C/C++
```
make ctest
./build/ctest
```

Or `make tests` to compile both.

## Building PyPI wheels
### Manual build
To manually build a PyPI wheel of the python package:
```
cd pydave
python setup.py bdist_wheel
```
Note that this will automatically build the fortran library and copy the .so file into the correct location, however it will not "audit" or "delocate" the wheel (i.e. copy in and relink any non-standard external libraries that are dependencies).

### Manual build + audit/delocate
The script `pydave/build-wheels.sh` will build and audit the wheel for you. However you must run this within the `pydave` directory.
```
cd pydave
./build-wheels.sh
```
This will create the audited/delocated wheel inside `wheelhouse/`
```
wheelhouse:
pydave-0.0.7-py3-none-macosx_10_9_x86_64.whl
```

### Manylinux
To build "manylinux" wheels, we use Docker. Just run this script
```
./docker-build-manylinux-wheels.sh
```
which will run `pydave/build-wheels.sh` inside a docker container for each manylinux image/platform.

### Manual install
If you wish, you can just install the python package into your environment without building a wheel
```
cd pydave
python setup.py install
```

To uninstall `pip uninstall <package-name>`.

## TestPyPI
1. To upload to TestPyPI `twine upload --repository testpypi wheelhouse/*`
2. To install somewhere `pip install --index-url https://test.pypi.org/simple/ --no-deps <package-name>`
