#!/bin/bash
# checkout and build aviz
set -e
git clone --branch master --depth 1 https://github.com/simphony/AViz.git
pushd AViz/src
qmake aviz.pro
make -j 2
popd
mkdir -p bin
cp AViz/src/aviz bin/.
rm -rf AViz
