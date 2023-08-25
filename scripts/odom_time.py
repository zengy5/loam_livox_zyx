#!/usr/bin/python3

import rospy
import numpy as np
from nav_msgs.msg import Odometry
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import PointCloud2

file_name = '/root/Loam_livox/time_frame.txt'
class Transformer():
    head_time = 0
    def __init__(self):
        self.sub = rospy.Subscriber('/laser_time', PointCloud2, self.trans, queue_size=1)
        
    def trans(self,data):
        #print(data)
        self.head_time = data.header.stamp.secs+ data.header.stamp.nsecs * 1e-8

        with open(file_name,'a') as file:
            file.write(str(self.head_time) + '\n')


if __name__=='__main__':
    rospy.init_node('lasertime')
    rospy.loginfo("Start recording time")
    with open(file_name,'a') as init:
        init.truncate(0)
    tf = Transformer()
    rospy.spin()
