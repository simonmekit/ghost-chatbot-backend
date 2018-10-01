import subprocess as sp



class Relex:
    def __init__(self):
        # change your relex server location here
        self.relex_location = "/home/aman/relex"
        self.isRelex = False
        self.startRelex()

    def startRelex(self):
        if not self.isRelex:
            print("----------opening relex server------------")
            try:
                sp.call('./opencog-server.sh', cwd='{}'.format(self.relex_location))
                print("Relex Server opened successfully")
                self.isRelex = True
            except ValueError as e:
                self.isRelex = False
                print("Error occured in opening relex server")
                exit(0)

serve = Relex()