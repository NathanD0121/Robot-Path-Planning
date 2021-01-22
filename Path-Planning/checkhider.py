#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from visualization_msgs.msg import Marker

markerx=10
markery=10
hiderstatus=0
def callback(msg):
   global hiderstatus
   if (abs(msg.pose.pose.position.x - markerx )< 1.5 and abs(msg.pose.pose.position.y - markery) <1.5 ):
	    hiderstatus = 1

def callback2(msg):
	global markerx
	global markery
	global pub
	markerx=msg.pose.position.x
	markery=msg.pose.position.y
	pub.publish(str(hiderstatus))

rospy.init_node('check_hider', anonymous=True)
odom_sub =rospy.Subscriber('/odom',Odometry,callback)
sub=rospy.Subscriber('/marker_basic',Marker,callback2)
pub = rospy.Publisher('/hider_status', String, queue_size=1)
rospy.spin()
