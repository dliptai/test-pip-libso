#!/bin/bash
set -e -x

# If MANLINUX is not set, assume no
if [ -z "$MANYLINUX" ]; then
  MANYLINUX=no
fi

#-- Script requires environment variable PLAT to be set
set -u

# Use manylinux pythons if MANYLINUX=yes
# otherwise use default system python
if [ "${MANYLINUX}" == "yes" ]; then
  PYTHONS=/opt/python/cp3*/bin/python
else
  PYTHONS=python
fi

OS=$(uname -s)

# Choose between delocate and auditwheel and the directory
# (within the package) to copy the external libraries to,
# depending on the system.
if [ "${OS}" == "Darwin" ]; then
  DELOCATE_TOOL='delocate-wheel'
  LIB_DIR=libs/.dylibs
else
  DELOCATE_TOOL='auditwheel repair'
  LIB_DIR=/libs/
fi

# Set directories for dirty and fixed wheels
DIST_DIR=wheels
WHEELHOUSE=wheels_fixed

# Clean out any old wheels in the dirty wheels folder
rm ${DIST_DIR}/*.whl || true

# Compile wheels
for PYTHON in $PYTHONS; do
  # Clean build dir
  ${PYTHON} setup.py clean --all
  rm src/libs/*.so || true
  # Create wheel
  ${PYTHON} setup.py bdist_wheel --plat-name ${PLAT} --dist-dir ${DIST_DIR}
done

# Delocate wheels (remove external lib dependencies by including relevant libs in wheel)
# Note: these tools also relink libraries for you by modifying their ELFs
for whl in ${DIST_DIR}/*.whl; do
  ${DELOCATE_TOOL} -L ${LIB_DIR} -w ${WHEELHOUSE} ${whl}
done
