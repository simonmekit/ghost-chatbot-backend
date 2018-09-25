import subprocess as sp
import os

from apighost import whole


class Relex:
    def __init__(self):
        self.isRelex = False
        self.startRelex()
        # self.proc = ""

    # def takeInput(self):
    #     self.startGuile()
    #     value = input("Please enter your rule or '(quit)' to exit: ")
    #     if value == "(quit)":
    #         found = input("Are you sure? Y or N: ")
    #         if found == "Y" or found == "y":
    #             raise SystemExit
    #         else:
    #             self.takeInput()
    #     self.ghostRule(value.encode())

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

        if self.isRelex:
            whole()


serve = Relex()