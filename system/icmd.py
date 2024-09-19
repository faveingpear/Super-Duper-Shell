from multiprocessing.connection import Listener
import time
import glob

class command_interpreter():

    def __init__(self, ip:str, port:int) -> None:
        self.ip = ip
        self.port = port
        self.load_modules("modules/")
        print("Starting command interpreter server")
        self.server(self.ip, self.port) 

    def server(self, ip, port):
        self.listener = Listener((ip, port))
        self.running = True
        while self.running:
            self.conn = self.listener.accept()
            while True:
                command = self.conn.recv()
                responce = self.interpret_command(command)
                self.send_responce(responce=responce)
                if command == "exit":
                    self.conn.close()
                    self.running = False
                    break

        self.listener.close()
    
    def send_responce(self,responce):
        self.conn.send(responce)
        
    
    def interpret_command(self,command:str)->str:
        command = command.split(" ")
        if command[0] == "computer":
            count = 1
            for i in range(100000000):
                count = count+1
            return str(count)
        elif command[0] == "exit":
            return "Closing connection"
        else:
            return "Command not found"

    def load_modules(self, module_path):
        files = glob.glob(module_path+"*.py")

        for file in files:
            code = None
            with open(file) as f:
                code = f.read()
                f.close()
            exec(code)

