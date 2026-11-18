#! /usr/bin/env python3
import socket
import rospy
import time
from puppy_control.msg import Velocity
from std_msgs.msg import String
from std_srvs.srv import Empty

command = ''

pub = None

def sosea(msg):
    vel_msg = Velocity(x=0,y=0,yaw_rate=0)
    global command, pub 
    
    local_command = msg.data
        
    if local_command == 'up':
        if local_command != command :
            vel_msg.x = 0 
            pub.publish(vel_msg)
            time.sleep(0.1)
            vel_msg.x = 20
            pub.publish(vel_msg)
        time.sleep(0.6)
    elif local_command == 'down':
        if local_command != command :
            vel_msg.x = 0 
            pub.publish(vel_msg)
            time.sleep(0.1)
            vel_msg.x = -20
            pub.publish(vel_msg)
        time.sleep(0.6)
    elif local_command == 'left':
        if local_command != command:
            vel_msg.x = 0
            vel_msg.yaw_rate = 0
            pub.publish(vel_msg)
            time.sleep(0.1)
            vel_msg.x = 7 
            vel_msg.yaw_rate = 0.4
            pub.publish(vel_msg)
        time.sleep(0.6) 
    elif local_command == 'right':
        if local_command != command:
            vel_msg.x = 0 
            vel_msg.yaw_rate = 0
            pub.publish(vel_msg)
            time.sleep(0.1)
            vel_msg.x = 7
            vel_msg.yaw_rate = -0.4
            pub.publish(vel_msg)
        time.sleep(0.6)
    elif local_command == 'look_up':
        if local_command != command:
            vel_msg.
    elif local_command == 'look_down':
        if local_command != command:

    elif local_command == '':
        if command !=local_command :
            vel_msg.x = 0 
            vel_msg.yaw_rate = 0 
            pub.publish(vel_msg)
            time.sleep(0.1)
    command = local_command    
     
        

if __name__ == '__main__':
    rospy.init_node("TweetyNODE", log_level = rospy.DEBUG)
    rospy.loginfo("Hello")
    rospy.ServiceProxy("/puppy_control/go_home", Empty)()
    pub = rospy.Publisher("/puppy_control/velocity", Velocity, queue_size = 1)
    rospy.Subscriber("Sylvester", String, sosea,queue_size = 1)
    rospy.spin()


