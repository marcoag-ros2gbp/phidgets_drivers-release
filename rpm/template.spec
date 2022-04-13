%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-phidgets-drivers
Version:        2.3.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS phidgets_drivers package

License:        BSD, LGPL
URL:            http://ros.org/wiki/phidgets_drivers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-libphidget22
Requires:       ros-rolling-phidgets-accelerometer
Requires:       ros-rolling-phidgets-analog-inputs
Requires:       ros-rolling-phidgets-api
Requires:       ros-rolling-phidgets-digital-inputs
Requires:       ros-rolling-phidgets-digital-outputs
Requires:       ros-rolling-phidgets-gyroscope
Requires:       ros-rolling-phidgets-high-speed-encoder
Requires:       ros-rolling-phidgets-ik
Requires:       ros-rolling-phidgets-magnetometer
Requires:       ros-rolling-phidgets-motors
Requires:       ros-rolling-phidgets-msgs
Requires:       ros-rolling-phidgets-spatial
Requires:       ros-rolling-phidgets-temperature
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
API and ROS drivers for Phidgets devices

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Apr 13 2022 Martin Günther <martin.guenther@dfki.de> - 2.3.0-1
- Autogenerated by Bloom

* Thu Feb 17 2022 Martin Günther <martin.guenther@dfki.de> - 2.2.2-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Martin Günther <martin.guenther@dfki.de> - 2.2.1-2
- Autogenerated by Bloom

