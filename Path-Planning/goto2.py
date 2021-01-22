#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
hiderstatus=0
def movebase_searcher():
    global hiderstatus
    numberofarea=1
    searcher = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    searcher.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "odom"
    goal.target_pose.header.stamp = rospy.Time.now()
    pha = [[4.0, 0.0, 1.0], [-4.0, 0.0 ,-1.0], [4.0, 4.0,1.0], [-4.0, 4.0, -1.0], [4.0, -4.0, 1.0], [-4.0, -4.0, -1.0]] #possible hiding areas
    for n in pha:
	      if hiderstatus != '1':
		      goal.target_pose.pose.position.x = n[0]
		      goal.target_pose.pose.position.y = n[1]
		      goal.target_pose.pose.orientation.z = n[2]
		      searcher.send_goal(goal)
		      wait = searcher.wait_for_result()
		      if not wait:
			 rospy.logerr("Fault!")
			 rospy.signal_shutdown("Fault!")
		      else:
			 print(numberofarea , '. area has been searched!')
			 numberofarea = numberofarea + 1
    return searcher.get_result
def callback(msg):
	global hiderstatus
	hiderstatus=msg.data
if __name__ == '__main__':
    try:
        rospy.init_node('movebase_searcher')
	sub=rospy.Subscriber('/hider_status',String,callback)
        result = movebase_searcher()
        if result:
	    print("I caught you. ")
            print("Let's play again!")
    except rospy.ROSInterruptException:
        rospy.loginfo("")
