^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package denso_launch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.3 (2018-04-24)
------------------

2.0.2 (2017-11-01)
------------------
* Fix kinetic-devel (denso_ros_control) for simulation usage (`#88 <https://github.com/start-jsk/denso/issues/88>`_)
  * test_moveit.py: sleep before retry go()
  * wait for /move_group/goal
  * re-enable vs060.test, add workaround for pyassimp, run go() twice
  * clean up launch file for newer demo.launch in vs060_moveit_config, which accepts dryrun argument
  * rm denso_vs060_startup\_*
  * update moveit configuration for new denso_ros_controller package
* [kinetic-devel] Update maintainer (`#85 <https://github.com/start-jsk/denso/issues/85>`_)
* Fix travis (`#87 <https://github.com/start-jsk/denso/issues/87>`_)
  * test/vs060 failing due to missing denso_controller
* Contributors: Isaac I.Y. Saito, Kei Okada

2.0.1 (2017-08-09)
------------------

2.0.0 (2017-08-09)
------------------
* fix CATKIN-DEPENDS -> CATKIN_DEPENDS
* denso_launch depends on denso_ros_control
* Contributors: Kei Okada

1.1.8 (2017-03-03)
------------------

1.1.7 (2016-08-23)
------------------

1.1.6 (2016-06-24)
------------------
* remove unnessesary depends
* Contributors: Kei Okada

1.1.5 (2016-04-05)
------------------
* install test directories
* Contributors: Kei Okada

1.1.4 (2016-02-08)
------------------
* fix xtion setings for real robots
* denso_launch/test, move denso_vs060_moveit_demo_test.py and add test for publish_simple_scene.py
* Contributors: Kei Okada

1.1.3 (2016-02-04)
------------------
* param name have cheanged single -> maxboard
* fix xtion settings for hydro+
* denso_launch: mv catkin.cmake -> CMakeList.txt
* add publish_simple_scene.py and fix test code
* remove demo_simulation_noenvironment: default launch is denso_vs060_moveit_demo_simulation.launch for dryrun, (i think...)
* Contributors: Kei Okada

1.1.2 (2015-12-21)
------------------
* denso_launch/test/vs060.test: move denso_vs060_moveit_demo_test.py to vs060.test
* denso_launch/test/vs060.test: do not have to check over 30sec,we need to wait to starting moveit, and test just for a second
* [vs060] Add simple unit test cases for moveit
* Contributors: Isaac I.Y. Saito, Kei Okada

1.1.1 (2015-11-03)
------------------

1.1.0 (2015-10-31)
------------------

1.0.0 (2015-10-30)
------------------
* update to indigo

0.2.9 (2015-03-07)
------------------

0.2.8 (2014-07-30)
------------------
* Add xtion checkerboard demo launch file.
* Add moveit_commander test
* Correct robot name (vs06 -> vs060)
* Add rostest for /denso_vs060_moveit_demo_simulation.launch
* Contributors: Isaac IY Saito, Kei Okada

0.2.7 (2014-01-03)
------------------
* Rename repository (Fix https://github.com/start-jsk/denso/issues/13, https://github.com/start-jsk/denso/issues/14)
* Contributors: Isao Isaac Saito

0.2.6 (2013-12-13)
------------------
* Remove manifest.xml since the entire package depends on wet packages open_industrial_ros_controllers.
* Contributors: Isao Isaac Saito

0.2.5 (2013-12-11)
------------------

0.2.4 (2013-12-10)
------------------

0.2.3 (2013-12-07)
------------------

0.2.2 (2013-12-06)
------------------

0.2.1 (2013-12-06)
------------------

0.2.0
-----------

* Init commit
* Contributors: Isao Isaac Saito
