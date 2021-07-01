import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3

def talker():
    pub = rospy.Publisher('my_vector', Vector3, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

    # tw_msg = Vector3()
    # tw_msg.x = 1.0
    # tw_msg.y = 2.0
    # tw_msg.z = 3.0
    tw_msg =Vector3(1.0,2.0,3.0)

    rospy.loginfo(tw_msg)
    rospy.loginfo("My vector is (%0.3f,%0.3f,%0.3f)" %(tw_msg.x,tw_msg.y,tw_msg.z))
    pub.publish(tw_msg)
    rate.sleep()

if __name__ == '__main__':

try:
talker()
except rospy.ROSInterruptException:
pass
