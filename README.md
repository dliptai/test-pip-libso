# Python package + shared object (.so library) test
This repo is a testing ground for building a shared object library, and then including this in a python package that can be uploaded to PyPI.

Basic idea/steps:

1. Declare a Fortran subroutine with "bind c" in `libdave.f90`
2. Compile this into a shared object library (.so) using `-shared` and `-fPIC` flags
3. Copy the library into a python package
4. Load the library using CDLL from ctypes, and create a python binding for the subroutine
5. Upload the python package to TestPyPI

## Fortran to shared object library
The Fortran library is in `libdave.f90`. It contains a subroutine declared with `bind(c)`.

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

## Building PyPI wheels
To manually build a PyPI wheel of the python package:
```
cd pydave
python setup.py bdist_wheel
```
Note that this will automatically build the fortran library and copy the .so file into the correct location.

To build "manylinux" wheels, we use Docker. Just run this script
```
./build-wheels.sh
```
which will run `docker/builder_manylinux.sh` inside a docker container for each manylinux image/platform.
