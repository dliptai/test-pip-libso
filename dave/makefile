FC = gfortran
CC = g++

#-- Make sure all source is compile with -fPIC (Position Independent Code) if you want to make a library
FFLAGS = -O3 -Wall -Wextra -pedantic -std=f2008 -fcheck=all
CFLAGS = -Wall

SRC = libdave.f90
OBJ=${SRC:.f90=.o}

LIBNAME=dave

%.o : %.f90
	$(FC) $(FFLAGS) -c $< -o $@

#-- Compile fortran source into a shared object (.so) library
lib: $(OBJ)
	$(FC) -shared -fPIC $(FFLAGS) $(OBJ) -o lib$(LIBNAME).so

#-- Compile a fortran test executable from the shared object
ftest: lib
	$(FC) $(FFLAGS) lib$(LIBNAME).so ftest.f90 -o $@

#-- Compile a c++ test executable from the shared object
ctest: lib
	$(CC) $(CFLAGS) -o $@ ctest.cpp -l$(LIBNAME) -L./

	# g++ -Wall -o test test.cpp -ltest -L/Users/dliptai/Work/testing/libso

clean:
	rm -f *.o *.mod *.smod test *.so ftest ctest
