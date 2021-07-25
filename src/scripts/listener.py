#!/usr/bin/env python3
import rospy
import warnings
# from std_msgs.msg import String
warnings.filterwarnings("ignore")
from testing.msg import custom

def callback(custom_message):
    rospy.loginfo(rospy.get_caller_id() + " I HEARD (%d %s)" , custom_message.id, custom_message.name)

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("chatter", custom, callback, queue_size=10)

    rospy.spin()

if __name__ == "__main__":
    listener()