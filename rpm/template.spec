%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-phidgets-digital-outputs
Version:        2.2.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS phidgets_digital_outputs package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-launch
Requires:       ros-galactic-phidgets-api
Requires:       ros-galactic-phidgets-msgs
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rclcpp-components
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake-ros
BuildRequires:  ros-galactic-phidgets-api
BuildRequires:  ros-galactic-phidgets-msgs
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rclcpp-components
BuildRequires:  ros-galactic-std-msgs
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Driver for the Phidgets Digital Output devices

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Thu Feb 17 2022 Martin Günther <martin.guenther@dfki.de> - 2.2.2-1
- Autogenerated by Bloom

* Tue Aug 03 2021 Martin Günther <martin.guenther@dfki.de> - 2.2.1-1
- Autogenerated by Bloom

* Thu May 20 2021 Martin Günther <martin.guenther@dfki.de> - 2.2.0-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Martin Günther <martin.guenther@dfki.de> - 2.1.0-2
- Autogenerated by Bloom

* Mon Mar 29 2021 Martin Günther <martin.guenther@dfki.de> - 2.1.0-1
- Autogenerated by Bloom

* Fri Mar 26 2021 Martin Günther <martin.guenther@dfki.de> - 2.0.2-3
- Autogenerated by Bloom

* Mon Mar 08 2021 Martin Günther <martin.guenther@dfki.de> - 2.0.2-2
- Autogenerated by Bloom

