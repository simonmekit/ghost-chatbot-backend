import subprocess as sp
import os
import sys


class whole:
    def __init__(self):
        self.isGuile = False
        self.ruleset = []
        self.repset = []
        self.proc = sp.Popen("guile", stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, bufsize=0)
        self.startGuile()
        self.takeInput()

    def takeInput(self):
        """

        :return:
        """
        while (True):
            value = input("Please enter your rule or '(quit)' to exit: ")
            if value == "(quit)":
                found = input("Are you sure? Y or N: ")
                if found == "Y" or found == "y":
                    raise SystemExit
                else:
                    break
            print(self.ruleCheck(value))
        self.takeInput()

    def startGuile(self):
        if not self.isGuile:
            print("--------------------starting GUILE----------------------")
            # self.proc = sp.Popen('guile', stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
            try:
                a = self.proc.stdout.readline()
                if "GNU Guile" in a:
                    print("Guile has successfully opened")
                else:
                    print("Guile Failed!")
                    exit(0)
            except Exception as e:
                print("Error occurred in starting guile: ", e)
        self.loadModules()
        self.testGuile()

    def loadModules(self):
        # loading modules
        try:
            modules = ""
            with open('module.txt', 'r') as f:
                for line in f:
                    modules += line
                # toByte = modules.encode()
                self.proc.stdin.write(modules)
                print("Modules successfully loaded from file")
        except Exception as e:
            print("Error occurred while trying to load modules from file: ", e)

    def testGuile(self):
        try:
            # Train from files
            self.proc.stdin.write("(ghost-parse-files \"./files.ghost\")")
            print("Trained file rules successfully")

        except Exception as e:
            print("Error occurred in testing rule: ", e)

    def ruleCheck(self, toString):
        # self.ruleset.append(toString)
        try:
            if '(ghost-parse-file' in toString or '(ghost-parse' in toString:
                self.ruleset.append(toString)
                self.executeRule(self.ruleset)
            elif toString == '':
                self.takeInput()
            else:
                inout = '(map cog-name (test-ghost \"{}\"))'.format(toString)
                self.ruleset.append(inout)
                self.executeRule(self.ruleset)

        except Exception as e:
            print("Error occurred in writing rule: ", e)

    def executeRule(self, rulecont):
        for i in rulecont:
            self.proc.stdin.write(i)
            for line in iter(self.proc.stdout.readline, ''):
                if "[GHOST]" in line:
                    self.repset.append(line)
        self.outputIT()

        # self.proc.stdin.close()

    def outputIT(self):
        for i,j in zip(self.ruleset,self.repset):
            print(i)
            print(j)


print("-------------Welcome-------------")
one = whole()
