Name:           ros-kinetic-vs060
Version:        2.0.2
Release:        0%{?dist}
Summary:        ROS vs060 package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/vs060
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-moveit-commander
Requires:       ros-kinetic-moveit-ros-planning
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslang
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-moveit-commander
BuildRequires:  ros-kinetic-moveit-ros-planning
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslang

%description
This package provides ORiN-based controller functionality for VS060, a Denso's
virtical multi-joint robot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Nov 01 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Wed Aug 09 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

