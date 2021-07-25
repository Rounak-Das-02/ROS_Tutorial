#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def talker():

    rospy.init_node("/turtle1/cmd_vel", Twist)
    while not rospy.is_shutdown():
        print("HI")





if __name__ == "__main__":
    talker()