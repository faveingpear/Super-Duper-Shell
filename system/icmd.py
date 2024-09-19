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
        if responce==None:
            self.conn.send("")

        self.conn.send(responce)
        
    
    def interpret_command(self,command:str)->str:
        command = command.split(" ")

        if command[0] == "help":
            if len(command) == 1:
                print("Help command")
            else:
                for cmd, module in self.modules:
                    if command[1] == cmd:
                        return module.help()

        for cmd, module in self.modules:
            if command[0] == cmd:
                if len(command) == 1:
                    return module.run()
                else:
                    return module.run(args=command[1:])

        return "Command not found"

    def load_modules(self, module_path):
        files = glob.glob(module_path+"*.py")

        self.modules = []
        for file in files:
            code = None
            ldict = {}
            with open(file) as f:
                code = f.read()
                f.close()
            exec(code, ldict)
            self.modules.append((ldict["module"].get_command(),ldict["module"]))
        print(self.modules)
