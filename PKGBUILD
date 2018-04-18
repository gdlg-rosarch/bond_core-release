# Script generated with Bloom
pkgdesc="ROS - C++ implementation of bond, a mechanism for checking when another process has terminated."
url='http://www.ros.org/wiki/bondcpp'

pkgname='ros-kinetic-bondcpp'
pkgver='1.8.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-kinetic-bond'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules>=0.3.2'
'ros-kinetic-roscpp'
'ros-kinetic-smclib'
'util-linux'
)

depends=('boost'
'ros-kinetic-bond'
'ros-kinetic-roscpp'
'ros-kinetic-smclib'
'util-linux'
)

conflicts=()
replaces=()

_dir=bondcpp
source=()
md5sums=()

prepare() {
    cp -R $startdir/bondcpp $srcdir/bondcpp
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

