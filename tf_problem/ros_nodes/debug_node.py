#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from tf2_msgs.msg import TFMessage


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(data))


def listener():

    rospy.init_node('listener', anonymous=True, log_level=rospy.DEBUG)
    rospy.Subscriber("tf", TFMessage, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
