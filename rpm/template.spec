Name:           ros-jade-bondpy
Version:        1.7.18
Release:        0%{?dist}
Summary:        ROS bondpy package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/bondpy
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       libuuid-devel
Requires:       ros-jade-rospy
Requires:       ros-jade-smclib
BuildRequires:  ros-jade-bond
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-smclib

%description
Python implementation of bond, a mechanism for checking when another process has
terminated.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.7.18-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.7.17-0
- Autogenerated by Bloom

* Wed Dec 31 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.7.16-0
- Autogenerated by Bloom

