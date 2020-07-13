VPATH=../src

# Compilers
FC=gfortran
CC=g++

#-- Make sure all source is compile with -fPIC (Position Independent Code) if you want to make a library
FFLAGS=-O3 -Wall -Wextra -pedantic -std=f2008 -fcheck=all -fPIC
CFLAGS=-Wall

#-- Shared library will look for depenedices in it's own directory,
#   if it can't find them in the system paths.
LIBFLAGS=-shared -Wl,-rpath,'$$ORIGIN'

#-- Some older BSD derivatives may ignore $ORIGIN if "-z origin" flag is not provided
#   (https://stackoverflow.com/questions/33853344/what-are-the-recommended-gnu-linker-options-to-specify-origin-in-rpath)
#   Adding it just to be safe, but probably unnecessary.
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
  LIBFLAGS += -Wl,-z,origin
endif

SRC=libdave.f90
OBJ=${SRC:.f90=.o}

LIBNAME=dave

%.o : %.f90
	$(FC) $(FFLAGS) -c $< -o $@

#-- Compile fortran source into a shared object (.so) library
lib: $(OBJ)
	$(FC) $(LIBFLAGS) $(FFLAGS) $(OBJ) -o lib$(LIBNAME).so

#-- Compile a fortran test executable from the shared object
ftest: lib
	$(FC) $(FFLAGS) lib$(LIBNAME).so ftest.f90 -o $@

#-- Compile a c++ test executable from the shared object
ctest: lib
	$(CC) $(CFLAGS) -o $@ ctest.cpp -l$(LIBNAME) -L./

tests: ftest ctest

test: tests

clean:
	rm -f *.o *.mod *.smod test *.so ftest ctest

.PHONY: lib tests test clean
