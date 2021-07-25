#!/usr/bin/env python3
import rospy
import random
# from std_msgs.msg import String
from testing.msg import custom
def talker():
    pub = rospy.Publisher("chatter", custom, queue_size=10)
    rospy.init_node("talker", anonymous=True)
    rate = rospy.Rate(1) ## 1 message per second
    count = 0
    while not rospy.is_shutdown():
        Custom_Mssg = custom()
        count+=1
        Custom_Mssg.id = count
        Custom_Mssg.humidity = random.randint(70, 100)
        Custom_Mssg.temperature = 10
        Custom_Mssg.name = "HELLO"
        rospy.loginfo(Custom_Mssg.id)
        pub.publish(Custom_Mssg)
        rate.sleep()


if __name__ == "__main__":
    try:
        print("HELLO")
        talker()
    except Exception as e:
        print(e)
        pass