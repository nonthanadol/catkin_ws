#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
global velx
global pose
velx = Twist()
pose = Pose()

def callback1(data):
        velx.linear.x = data.linear.x

def callback2(data):
        pose.x = data.x   

def listener():
    rospy.init_node('subturtle1', anonymous=True)
    rospy.Subscriber('/turtle1/cmd_vel', Twist,callback1)
    rospy.Subscriber('/turtle1/pose', Pose,callback2)
    rate = rospy.Rate(4)
    while not rospy.is_shutdown():
        print('linear velocity x : {} ' .format(velx.linear.x))
        print('Position x : {} ' .format(pose.x))

        #rospy.loginfo(velx.linear.x)
        #rospy.loginfo(pose.x)
        
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    listener()
