import glob

class mod():

    def __init__(self) -> None:
        self.command = "mintpy"
        self.name = "Testing"
        self.has_args = True

    def run(self, args=None):
        print(args)
        return None

    def getname(self):
        return self.name

    def __str__(self) -> str:
        return "TESTING"
    
    def get_command(self):
        return self.command

    def help(self)->str:
        msg = """
        args:
            -r reminder
            -t time
        """
        return msg
module = mod()