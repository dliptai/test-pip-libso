# Fortran to shared object library
The Fortran library is in `libdave.f90`. It contains a subroutine declared with `bind(c)`.

To compile this into a shared object library, type `make` or `make lib`.

## Tests
To test that the function is callable from the library in Fortran type
```
make ftest
./ftest
```

Similarly to test that it's callable in C/C++
```
make ctest
./ctest
```
