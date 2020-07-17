#!/bin/bash
set -e -u -x

cd /io/pydave
LIB_DIR=./src/libs
TMP_WHEELHOUSE=./tmp_wheelhouse

# Compile wheels
for PYTHON in /opt/python/cp37*/bin/python; do
  # Clean build dir
  "${PYTHON}" setup.py clean --all

  # Make sure temporary wheel folder is empty
  rm "${TMP_WHEELHOUSE}"/*.whl || true

  # Create temporary wheel
  "${PYTHON}" setup.py bdist_wheel --dist-dir "${TMP_WHEELHOUSE}"

  # Run auditwheel to find external dependencies, then copy to LIB_DIR
  auditwheel -v show "${TMP_WHEELHOUSE}"/*.whl 2> /dev/null | "${PYTHON}" auditwheel_libcopy.py "${LIB_DIR}"

  # Rebuild wheel
  "${PYTHON}" setup.py bdist_wheel --plat $PLAT
done

# Clean libs folder
rm ${LIB_DIR}/*.so* || true
rm ${LIB_DIR}/*.dylib* || true
rm -rf tmp_wheelhouse || true
