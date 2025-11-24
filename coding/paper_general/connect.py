#!/usr/bin/env python3
import socket
import time

HOST = '94.237.120.119'
PORT = 35133

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((HOST, PORT))
        print("Connected!")
        
        # Try sending a newline to trigger response
        s.sendall(b"\n")
        time.sleep(0.5)
        
        try:
            data = s.recv(4096).decode('utf-8', errors='ignore')
            print(f"Received: {data}")
        except socket.timeout:
            print("No response")
            
        # Try sending "1"
        s.sendall(b"1\n")
        time.sleep(0.5)
        
        try:
            data = s.recv(4096).decode('utf-8', errors='ignore')
            print(f"Received: {data}")
        except socket.timeout:
            print("No response")
            
if __name__ == "__main__":
    connect()
