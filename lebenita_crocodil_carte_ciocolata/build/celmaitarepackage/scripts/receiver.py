#! /usr/bin/env python3
import socket
import rospy
import time
from puppy_control.msg import Velocity
from std_msgs.msg import String



def server_program():
    host = "0.0.0.0"
    port = 6767
    rate = rospy.Rate(30)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))

        server_socket.listen()
        conn, address = server_socket.accept()
        
        conn.setblocking(0)

        command = ""
        
        while not rospy.is_shutdown():
            try:
                lines = conn.recv(1024).decode('utf-8').split("\n")
                if len(lines)> 1:
                        command = lines[-2]
            except:
                command = ""
            
            pub.publish(command)            
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node("WHATEVERNODE", log_level = rospy.DEBUG)
    rospy.loginfo("Hello")   
    pub = rospy.Publisher('Sylvester',String,queue_size = 1)
   
    #rospy.spin()
    server_program()

