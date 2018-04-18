# Script generated with Bloom
pkgdesc="ROS - The State Machine Compiler (SMC) from http://smc.sourceforge.net/ converts a language-independent description of a state machine into the source code to support that state machine. This package contains the libraries that a compiled state machine depends on, but it does not contain the compiler itself."
url='http://smc.sourceforge.net/'

pkgname='ros-lunar-smclib'
pkgver='1.8.1_1'
pkgrel=1
arch=('any')
license=('Mozilla Public License Version 1.1'
)

makedepends=('ros-lunar-catkin'
)

depends=()

conflicts=()
replaces=()

_dir=smclib
source=()
md5sums=()

prepare() {
    cp -R $startdir/smclib $srcdir/smclib
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

