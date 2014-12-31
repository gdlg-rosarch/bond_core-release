Name:           ros-jade-smclib
Version:        1.7.16
Release:        0%{?dist}
Summary:        ROS smclib package

Group:          Development/Libraries
License:        Mozilla Public License Version 1.1
URL:            http://smc.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  ros-jade-catkin

%description
The State Machine Compiler (SMC) from http://smc.sourceforge.net/ converts a
language-independent description of a state machine into the source code to
support that state machine. This package contains the libraries that a compiled
state machine depends on, but it does not contain the compiler itself.

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
* Wed Dec 31 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.7.16-0
- Autogenerated by Bloom

