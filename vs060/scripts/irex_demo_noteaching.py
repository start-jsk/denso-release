#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2013, Tokyo Opensource Robotics Kyokai Association
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Tokyo Opensource Robotics Kyokai Association. nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Isaac Isao Saito

## THIS IS A COPY FROM irex_demo.py, removing reading dead-man switch from pendant

#%Tag(FULLTEXT)%

## workaround until https://github.com/ros-planning/moveit/pull/581 is released
import sys
sys.modules["pyassimp"] = sys
import pyassimp


import os
from subprocess import check_call

import actionlib_msgs.msg
from geometry_msgs.msg import Pose, PoseStamped, Point, Quaternion
from moveit_commander import MoveGroupCommander, conversions
from rospkg import RosPack
import roslib
import rospy
import std_msgs.msg
from tf.transformations import quaternion_from_euler
#roslib.load_manifest("denso_pendant_publisher")
#roslib.load_manifest("actionlib_msgs")

rospy.init_node("test_vs060_moveit")

arm = MoveGroupCommander("manipulator")
running_pub = rospy.Publisher("/irex_demo_running", std_msgs.msg.Bool);
#cancel_pub = rospy.Publisher("/arm_controller/follow_joint_trajectory/cancel", actionlib_msgs.msg.GoalID);
cancel_pub = rospy.Publisher("/move_group/cancel", actionlib_msgs.msg.GoalID);

# Get paths for files used later.
_rospack = RosPack()
SCENE_FILE = _rospack.get_path('vs060') + '/model/irex_model.scene'
_path_rosroot = rospy.get_ros_root()
_len_cut = len(_path_rosroot) - len('/share/ros')  # This is used to get ros root path /opt/%DISTRO% path.
_path_rosroot_top = _path_rosroot[:_len_cut]
LOAD_SCENE_PROG = _path_rosroot_top + '/lib/vs060/publish_scene_from_text'

print 'SCENE_FILE=', SCENE_FILE
print 'LOAD_SCENE_PROG=', LOAD_SCENE_PROG

def demo() :
    # load scene
    check_call([LOAD_SCENE_PROG, SCENE_FILE])
    for p in [[ 0.35, -0.35, 0.4],
              [ 0.6,  0.0, 0.4],
              [ 0.35,  0.35, 0.4],
              [ 0.6,  0.0, 0.2],
              [ 0.4,  0.0, 0.8]]:
        if True:
            print "set_pose_target(", p, ")"
            pose = PoseStamped(header = rospy.Header(stamp = rospy.Time.now(), frame_id = '/BASE'),
                               pose = Pose(position = Point(*p),
                                           orientation = Quaternion(*quaternion_from_euler(1.57, 0, 1.57, 'sxyz'))))

            arm.set_pose_target(pose)
            arm.go() or arm.go() or rospy.logerr("arm.go fails")
            rospy.sleep(1)
            if rospy.is_shutdown():
                return

if __name__ == "__main__":
    while not rospy.is_shutdown():
        demo()
#%EndTag(FULLTEXT)%
