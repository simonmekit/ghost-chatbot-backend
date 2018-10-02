import subprocess as sp

class Relex:
    def __init__(self):
        self.isRelex = False
        self.startRelex()

    def startRelex(self):
        if not self.isRelex:
            print("Opening Relex Server...")
            relexloc = input("Please enter the location of your relex folder:")
            try:
                sp.call('./opencog-server.sh', cwd='{}'.format(relexloc))
                print("Relex Server opened successfully")
                self.isRelex = True
            except ValueError as e:
                self.isRelex = False
                print("Error occured in opening relex server")
                exit(0)

serve = Relex()