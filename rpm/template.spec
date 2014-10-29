Name:           ros-hydro-bondcpp
Version:        1.7.15
Release:        0%{?dist}
Summary:        ROS bondcpp package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/bondcpp
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libuuid-devel
Requires:       ros-hydro-bond
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-smclib
BuildRequires:  boost-devel
BuildRequires:  libuuid-devel
BuildRequires:  ros-hydro-bond
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules >= 3.2.0
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-smclib

%description
C++ implementation of bond, a mechanism for checking when another process has
terminated.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Oct 29 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.7.15-0
- Autogenerated by Bloom

