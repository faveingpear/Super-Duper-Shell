#!/usr/bin/env python3

import multiprocessing
import multiprocessing.connection
from system.icmd import command_interpreter
import time

class shell():

    def __init__(self, ip:str, port:int) -> None:
        self.ip = ip
        self.port = port

    def spawn_cmd(self, ip:str, port:int):
        self.cmd = command_interpreter(ip, port)

    def run(self):
        self.cmdp = multiprocessing.Process(target=self.spawn_cmd, args=(self.ip,self.port))
        self.cmdp.start()

        time.sleep(0.5)

        self.conn = multiprocessing.connection.Client((self.ip, self.port))

        while True:
            command = input("Enter command:")
            self.send_command(command)
            responce = self.receive_responce()
            print(responce)
            time.sleep(0.1)

            if command=="exit":
                print("Goodbye")
                self.conn.close()
                exit()

    
    def send_command(self,command:str):
        self.conn.send(command)
    
    def receive_responce(self):
        response = self.conn.recv()
        return response

if __name__ == "__main__":
    sh = shell("localhost", 9999)
    sh.run()