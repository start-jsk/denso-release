Name:           ros-kinetic-denso
Version:        2.0.1
Release:        0%{?dist}
Summary:        ROS denso package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/denso
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-denso-launch
Requires:       ros-kinetic-denso-ros-control
Requires:       ros-kinetic-vs060
Requires:       ros-kinetic-vs060-gazebo
Requires:       ros-kinetic-vs060-moveit-config
BuildRequires:  ros-kinetic-catkin

%description
Packages in the denso suite provide controller functionality for Denso's
industrial manipulators. ORiN (Open Robot interface for the Network) is a
unified network interface for industrial robot applications and has been stably
utilized in Denso's manipulators for years. Controllers in this package suite
uses b-CAP, UDP-based control protocol defined in ORiN. It also has mechanism to
detect faulty commands. Using b-CAP, ROS communicates to the embedded controller
computer that has been achieving industry-proven reliability. The computer also
has mechanism to detect faulty commands. That said as a whole the system
maintains the same level of safeness with their commercial product setting.
Also, as a genuine ROS package, it enables robot application developers to
access full ROS features. MoveIt! configuration package is also included for
some of Denso's robots. Core functionality

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
* Wed Aug 09 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

