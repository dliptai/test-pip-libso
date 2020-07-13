#!/bin/bash
set -e -u -x

if [[ "$ARCH" == "x86_64" ]]; then
  X=64
else
  X=
fi

LIB_DIR=src/libs

cd /io/pydave

# Make copy of libgfortran.so to include in wheel
cp /usr/lib${X}/libgfortran.so.? ${LIB_DIR}/.

# Compile wheels
for PYBIN in /opt/python/cp3*/bin; do
  "${PYBIN}/python" setup.py bdist_wheel --plat $PLAT
done

# Clean libs folder
rm ${LIB_DIR}/*.so*