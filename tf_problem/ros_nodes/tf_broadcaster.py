#!/usr/bin/env python  
import rospy

import tf

def broadcast_pose():
    br = tf.TransformBroadcaster()
    br.sendTransform((10, 20, 0),
                     tf.transformations.quaternion_from_euler(0, 0, 1.5),
                     rospy.Time.now(),
                     'test_pose',
                     'world')

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster', anonymous=True)
    
    while True:
        broadcast_pose()
        rospy.sleep(0.5)
