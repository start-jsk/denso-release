Name:           ros-indigo-vs060-moveit-config
Version:        1.1.8
Release:        0%{?dist}
Summary:        ROS vs060_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/vs060_moveit_config
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-visualization
Requires:       ros-indigo-pr2-moveit-plugins
Requires:       ros-indigo-robot-mechanism-controllers
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-vs060
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-moveit-planners-ompl
BuildRequires:  ros-indigo-moveit-ros-move-group
BuildRequires:  ros-indigo-moveit-ros-visualization
BuildRequires:  ros-indigo-pr2-moveit-plugins
BuildRequires:  ros-indigo-robot-mechanism-controllers
BuildRequires:  ros-indigo-robot-state-publisher

%description
An automatically generated package with all the configuration and launch files
for using the vs060A1_AV6_NNN_NNN with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 03 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.8-0
- Autogenerated by Bloom

* Tue Aug 23 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.7-0
- Autogenerated by Bloom

* Fri Jun 24 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.6-0
- Autogenerated by Bloom

* Tue Apr 05 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.5-0
- Autogenerated by Bloom

* Mon Feb 08 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.4-0
- Autogenerated by Bloom

* Thu Feb 04 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.3-0
- Autogenerated by Bloom

* Mon Dec 21 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.2-0
- Autogenerated by Bloom

* Tue Nov 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.1-0
- Autogenerated by Bloom

* Sat Oct 31 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.0-0
- Autogenerated by Bloom

* Sat Mar 14 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.9-0
- Autogenerated by Bloom

