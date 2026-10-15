from pynput import keyboard
import socket

ROBOT_IP = "192.168.149.1"
PORT = 6767

keys_we_love = {
    'w': "up",
    'a': "left",
    's': "down",
    'd': "right",
    'Key.up': "up",
    'Key.down': "down",
    'Key.left': "left",
    'Key.right': "right",
    'Key.esc': "escape",
    'Key.space': "pause"
}


def on_press(key):
    try:
        char = key.char.lower()
    except AttributeError:
        char = format(key)

    if char in keys_we_love:
        message = keys_we_love[char]
        client_socket.sendall((message + "\n").encode())
        received_message = client_socket.recv(1024)
        print(received_message.decode('utf-8'))


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((ROBOT_IP, PORT))

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()