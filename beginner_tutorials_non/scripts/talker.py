#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(sys.version)
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()#time.sleep

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
