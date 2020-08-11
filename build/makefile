VPATH=../src
BINDIR=../bin

# Compilers
FC=gfortran
CC=g++

# Rememeber: -fPIC => Position Independent Code. (for shared libraries)
FFLAGS=-Wall -std=f2008 -fPIC
CFLAGS=-Wall -fPIC
LIBFLAGS=-shared

LIBNAME=dave
LIB=lib${LIBNAME}.so

#-- Look for depenedices in the directory where the binary file is located
#   (if it can't find them in the standard system paths)
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
  LDFLAGS=-Wl,-rpath,'$$ORIGIN'
  LDFLAGS += -Wl,-z,origin
  MAC_LIBFLAGS=
else ifeq ($(UNAME_S),Darwin)
  LDFLAGS=-Wl,-rpath -Wl,@loader_path
  MAC_LIBFLAGS=-install_name @rpath/$(LIB)
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
	$(FC) $(LIBFLAGS) $(MAC_LIBFLAGS) $(FFLAGS) $< -o $@
	cp $@ $(BINDIR)/.

#-- Compile a fortran test executable from the shared object
ftest: lib ftest.o
	$(FC) $(FFLAGS) ftest.o $(LDFLAGS) $(LIB) -o $@
	cp $@ $(BINDIR)/.

#-- Compile a c++ test executable from the shared object
ctest: lib ctest.o
	$(CC) $(CFLAGS) ctest.o $(LDFLAGS) -l$(LIBNAME) -L. -o $@
	cp $@ $(BINDIR)/.

tests: ftest ctest

test: tests

clean:
	rm -f *.o *.mod *.smod test *.so ftest ctest

.PHONY: lib tests test clean
