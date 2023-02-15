#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def print_data(data):
    rospy.loginfo(f"Print data x: {data.theta}")

if __name__ == "__main__":
    rospy.init_node("get_pose", anonymous=False)
    rospy.Subscriber("/turtle1/pose", Pose, print_data)
    rospy.spin()