#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry,OccupancyGrid
def callback(msg):
   #bool worldToMap(double wx, double wy, unsigned int& mx, unsigned int& my) const;
   print(msg)


rospy.init_node('check_odometry', anonymous=True)
odom_sub =rospy.Subscriber('/odom',OccupancyGrid,callback)

rospy.spin()
