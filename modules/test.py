import glob

class mod():

    def __init__(self) -> None:
        self.command = "ls"
        self.name = "Testing"
        self.has_args = False

    def run(self, args=None)->str:
        responce = ""

        responce = glob.glob(args[0])

        return responce

    def getname(self):
        return self.name

    def __str__(self) -> str:
        return "TESTING"
    
    def get_command(self):
        return self.command

module = mod()