import subprocess as sp
import os
import sys


class whole:
    def __init__(self):
        self.isGuile = False
        self.proc = ""
        self.takeInput()

    def takeInput(self):
        self.startGuile()
        while(True):
            value = input("Please enter your rule or '(quit)' to exit: ")
            if value == "(quit)":
                found = input("Are you sure? Y or N: ")
                if found == "Y" or found == "y":
                    raise SystemExit
                else:
                    self.takeInput()
            print(self.ghostRule(value.encode()))


    def startGuile(self):
        if not self.isGuile:
            print("--------------------starting GUILE----------------------")
            self.proc = sp.Popen('guile', stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
            try:
                a = self.proc.stdout.readline()
                if "GNU Guile" in a.decode():
                    print("Guile successfully opened")
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
                toByte = modules.encode()
                self.proc.stdin.write(toByte)
                print("Modules successfully loaded from file")
        except Exception as e:
            print("Error occurred while trying to load modules from file: ", e)

    def testGuile(self):
        try:
            code = b"""
                    (ghost-parse "u: (hello) hi there")
                    """
            self.proc.stdin.write(code)
            # print(self.proc.stdout.readline())
            test = b"""
                    (map cog-name (test-ghost "hello"))
                    """
            g = self.proc.stdin.write(test)
            print("Test completed successfully!")
            #Train from files
            replay = self.proc.stdin.write(b"""(ghost-parse-files \"./files.ghost\")""")
            print("Trained file rules successfully")
            # with open('opencog.log', 'rw') as f:
            # opencog.self.proc.communicate().
            # opencog.self.proc.communicate()
        except Exception as e:
            print("Error occurred in testing rule: ", e)

    def ghostRule(self, rule):
        try:
            toString = rule.decode()
            if 'ghost-parse-file' in toString or 'ghost-parse' in toString:
                print(self.proc.stdin.write(toString))
                # print(self.proc.stdout.)
            elif toString != '':
                rule = '(map cog-name (test-ghost \"{}\"))'.format(toString)
                print(self.proc.stdin.write(rule.encode()))
                # print(self.proc.stdout.communicate())
                # return self.proc.stdout.readline()
            else: self.takeInput()
        except Exception as e:
            print("Error occurred in writing rule: ", e)


print("-------------Welcome-------------")
one = whole()
