#!/bin/bash
set -e -u -x

# Launch a docker container and run build script in each manylinux image
for V in 1 2010 2014; do
  for ARCH in i686 x86_64; do
    PLAT="manylinux${V}_${ARCH}"
    DOCKER_IMAGE="quay.io/pypa/${PLAT}"
    docker run --rm -e MANYLINUX=yes -v `pwd`:/io -w /io/pydave $DOCKER_IMAGE /io/pydave/build-wheels.sh
  done
done
