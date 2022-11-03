#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   if ord(ch) == 3: quit() # handle ctrl+C
   return ch

if __name__ == '__main__':
	rospy.init_node('comando')
	pub = rospy.Publisher("/comando",String,queue_size=1)
	rate = rospy.Rate(2)
	while not rospy.is_shutdown():
		msg = String()
		msg.data = getchar()
		pub.publish(msg)
		rate.sleep()
		
	rospy.loginfo("Aplicacao Encerrada!")
