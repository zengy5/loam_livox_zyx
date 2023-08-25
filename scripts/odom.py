#!/usr/bin/python3

import rospy
import numpy as np
from nav_msgs.msg import Odometry
from sensor_msgs.msg import CompressedImage

file_name = '/root/Loam_livox/key_frame.txt'
class Transformer():
    pose_four = np.zeros(4)
    pose_t = np.zeros(3)
    head_time = 0
    def __init__(self):
        self.sub = rospy.Subscriber('/aft_mapped_to_init', Odometry, self.trans, queue_size=1)
        #self.subp = rospy.Subscriber('/camera1/color/image_raw/compressed', CompressedImage, self.times, queue_size=1)
        
    def times(self,img):
        self.head_time = img.header.stamp.secs+ img.header.stamp.nsecs * 1e-8

    def trans(self,data):
        #print(data)
        self.pose_four[0] = data.pose.pose.orientation.x  # quaternion x
        self.pose_four[1] = data.pose.pose.orientation.y  # quaternion y
        self.pose_four[2] = data.pose.pose.orientation.z  # quaternion z
        self.pose_four[3] = data.pose.pose.orientation.w  # quaternion w
        self.pose_t[0] = data.pose.pose.position.x        # offset x
        self.pose_t[1] = data.pose.pose.position.y        # offset x
        self.pose_t[2] = data.pose.pose.position.z        # offset x
        self.head_time = data.header.stamp.secs+ data.header.stamp.nsecs * 1e-8

        with open(file_name,'a') as file:
            file.write(str(self.head_time) + ' ' 
                    + str(self.pose_four[0])+ ' ' + str(self.pose_four[1])+ ' ' + str(self.pose_four[2])+ ' ' + str(self.pose_four[3]) + ' ' 
                    + str(self.pose_t[0])+ ' ' + str(self.pose_t[1])+ ' ' + str(self.pose_t[2]) + '\n')


if __name__=='__main__':
    rospy.init_node('transform')
    rospy.loginfo("Start recording")
    with open(file_name,'a') as init:
        init.truncate(0)
    tf = Transformer()
    rospy.spin()
