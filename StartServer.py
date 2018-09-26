import subprocess as sp



class Relex:
    def __init__(self):
        self.isRelex = False
        self.startRelex()
        # self.proc = ""

    def startRelex(self):
        if not self.isRelex:
            print("----------opening relex server------------")
            try:
                sp.call("./opencog-server.sh", cwd="/home/brook/Documents/relex/")
                print("Relex Server opened successfully")
                self.isRelex = True
            except ValueError as e:
                self.isRelex = False
                print("Error occured in opening relex server")
                exit(0)

serve = Relex()