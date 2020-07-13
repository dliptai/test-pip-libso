VPATH=../src

# Compilers
FC=gfortran
CC=g++

# Rememeber: -fPIC => Position Independent Code. (for shared libraries)
FFLAGS=-Wall -std=f2008 -fPIC
CFLAGS=-Wall -fPIC

LIBNAME=dave
LIB=lib${LIBNAME}.so

#-- Shared library will look for depenedices in it's own directory,
#   if it can't find them in the standard system paths.
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
  LDFLAGS=-Wl,-rpath,'$$ORIGIN'
  LDFLAGS += -Wl,-z,origin
  LIBFLAGS=-shared
else ifeq ($(UNAME_S),Darwin)
  LDFLAGS=-Wl,-rpath -Wl,@loader_path
  LIBFLAGS=-shared -install_name @rpath/$(LIB)
endif
#   Note: some older BSD derivatives may ignore $ORIGIN if "-z origin" flag is not provided
#   (https://stackoverflow.com/questions/33853344/what-are-the-recommended-gnu-linker-options-to-specify-origin-in-rpath)
#   Adding it just to be safe, but probably unnecessary.

%.o : %.f90
	$(FC) $(FFLAGS) -c $< -o $@

%.o : %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

lib: $(LIB)

#-- Compile fortran source into a shared object (.so) library
$(LIB): libdave.o
	$(FC) $(LIBFLAGS) $(LDFLAGS) $(FFLAGS) $< -o $@

#-- Compile a fortran test executable from the shared object
ftest: lib ftest.o
	$(FC) $(FFLAGS) $(LDFLAGS) $(LIB) ftest.o -o $@

#-- Compile a c++ test executable from the shared object
ctest: lib ctest.o
	$(CC) $(CFLAGS) $(LDFLAGS) -l$(LIBNAME) -L. ctest.o -o $@

tests: ftest ctest

test: tests

clean:
	rm -f *.o *.mod *.smod test *.so ftest ctest

.PHONY: lib tests test clean
