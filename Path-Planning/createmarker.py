#!/usr/bin/env python
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
import random

pha = [[4.5, 0.0, 1.0], [-4.5, 0.0 ,-1.0], [4.5, 4.5,1.0], [-4.5, 4.5, -1.0], [4.5, -4.5, 1.0], [-4.5, -4.5, -1.0]]

class MarkerBasics(object):
	def __init__(self):
		self.marker_objectlisher= rospy.Publisher('/marker_basic', Marker, queue_size=1)
		self.rate =rospy.Rate(1)
		self.init_marker(index=0, z_val=0)
	def init_marker(self, index=0,z_val=0):
		global pha
		s = random.randint(0, 5)
		self.marker_object = Marker()
		self.marker_object.header.frame_id = "/odom"
		self.marker_object.header.stamp = rospy.get_rostime()
		self.marker_object.ns = "some_robot"
		self.marker_object.id = index
		self.marker_object.type = Marker.SPHERE
		self.marker_object.action = Marker.ADD

		my_point = Point()
		my_point.z = z_val
		self.marker_object.pose.position.x = pha[s][0]
		self.marker_object.pose.position.y = pha[s][1]
		self.marker_object.pose.orientation.x = 0
		self.marker_object.pose.orientation.y = 0
		self.marker_object.pose.orientation.z = 0.0
		self.marker_object.pose.orientation.w = pha[s][2]
		self.marker_object.scale.x = 0.5
		self.marker_object.scale.y = 0.5
		self.marker_object.scale.z = 0.5
		
		self.marker_object.color.r = 0.0
		self.marker_object.color.g = 0.0
		self.marker_object.color.b = 1.0
		self.marker_object.color.a = 1.0
		self.marker_object.lifetime = rospy.Duration(0)
	
	def start(self):
		while not rospy.is_shutdown():
			self.marker_objectlisher.publish(self.marker_object)
			self.rate.sleep()

if __name__=='__main__':
	rospy.init_node('marker_basic_node' , anonymous=True)
	markerbasics_object = MarkerBasics()
	try:
		markerbasics_object.start()
	except rospy.ROSInterruptException:
		pass	
