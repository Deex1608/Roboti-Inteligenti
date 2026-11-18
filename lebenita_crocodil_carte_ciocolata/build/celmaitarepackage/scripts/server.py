#! /usr/bin/env python3
import socket
import rospy
import time
from puppy_control.msg import Velocity
from threading import Thread, Lock

command = ''
lock = Lock()

def sosea():
    global command
    pub = rospy.Publisher('/puppy_control/velocity',Velocity,queue_size = 1)
    vel_msg = Velocity(x=0,y=0,yaw_rate=0)

    while True:
        lock.acquire()
        local_command = command
        command = ''
        lock.release()
        
        if local_command == 'up':
            vel_msg.x = 20
            pub.publish(vel_msg)
            time.sleep(1)
            vel_msg.x = 0
            pub.publish(vel_msg)

        elif local_command == 'down':
            vel_msg.x = -10
            pub.publish(vel_msg)
            time.sleep(1)
            vel_msg.x = 0
            pub.publish(vel_msg)

        elif local_command == 'left':
            vel_msg.x = 7
            vel_msg.yaw_rate = 0.4
            pub.publish(vel_msg)
            time.sleep(1)
            vel_msg.x = 0
            vel_msg.yaw_rate=0
            pub.publish(vel_msg)
        
        elif local_command == 'right':
            vel_msg.x = 7
            vel_msg.yaw_rate = -0.4
            pub.publish(vel_msg)
            time.sleep(1)
            vel_msg.x = 0
            vel_msg.yaw_rate=0
            pub.publish(vel_msg)
        
     
        


def server_program():
    host = "0.0.0.0"
    port = 6767
    
    global command

        
    th = Thread(target=sosea, daemon = True)
    th.start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))

        server_socket.listen()
        conn, address = server_socket.accept()

        buff = ""
        
        while True:
            raw = conn.recv(1024)
            if not raw:
                break
            try:
                data = raw.decode('utf-8')
                buff += data
            except UnicodeDecodeError:
                continue
            except InterruptedError:
                break

            lock.acquire()
            command,end,buff = buff.partition("\n")
            lock.release()
            
            rospy.loginfo(command)
            conn.sendall(("Received " + command).encode())

if __name__ == '__main__':
    rospy.init_node("WHATEVERNODE", log_level = rospy.DEBUG)
    rospy.loginfo("Hello")
    #rospy.spin()
    server_program()

