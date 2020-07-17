#!/bin/bash
set -e -u

WHEEL=$1
LIBS_PATH=$2
libs=$(delocate-listdeps "${WHEEL}")
for L in $libs; do
   echo "Copying $L to $2/."
   cp $L $2/.
done
