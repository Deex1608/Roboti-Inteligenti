#! /usr/bin/env python3
import socket
import rospy

def server_program():
    host = "0.0.0.0"
    port = 6767

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


            command,end,buff = buff.partition("\n")
            rospy.loginfo(command)
            conn.sendall(("Received " + command).encode())

if __name__ == '__main__':
    rospy.init_node("WHATEVERNODE", log_level = rospy.DEBUG)
    rospy.loginfo("Hello")
    #rospy.spin()
    server_program()

