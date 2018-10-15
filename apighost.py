import subprocess as sp
import argparse

class whole:
    def __init__(self):
        self.all_rule = []
        self.all_answer = []
        self.running_times = 0
        self.question_file = open("files/cache.txt", "a+")
        self.disp = ""
        self.file_dir = 'files/files.ghost'
        self.args = ''

    def get_arguments(self):
        parser = argparse.ArgumentParser(description='Api ghost')
        parser.add_argument('--file_dir', type=str, default=self.file_dir,
                            help = 'The directory containing the training ghost file')

        return parser.parse_args()

    def takeInput(self):
        self.args = self.get_arguments()
        self.displayPopen()
        while True:
            self.running_times += 1
            value = input("Please enter your rule or '(quit)' to exit: ")
            if value == "(quit)":
                found = input("Are you sure? Y or N: ")
                if found == "Y" or found == "y":
                    self.question_file.close()
                    raise SystemExit
                elif found == "N" or found == "n":
                    continue
            self.ghostRule(value.encode())

    def displayPopen(self):
        self.disp = sp.Popen('guile', stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
        try:
            a = self.disp.stdout.readline()
            if "GNU Guile" in a.decode():
                if self.running_times == 0:
                    print("Guile Successfully Opened!")
            else:
                print("An error has occurred on Guile.")
        except Exception as e:
            print("Error occurred when starting guile: ", e)

        self.loadmodules()
        self.loadrules(self.args.file_dir)
        self.testguile()

        list_of_rules = self.all_rule
        aa = len(list_of_rules)
        try:
            i = 0
            while i <= aa - 1:
                if i == aa - 1:
                    stdou, stder = self.disp.communicate(input=list_of_rules[aa - 1].encode())
                    result_to_list = stdou.decode().split('\n')
                    answer = []
                    index = 0
                    while index < len(result_to_list):
                        if "[GHOST]" in result_to_list[index] \
                                or "<unnamed port>" in result_to_list[index] \
                                or "<unspecified>" in result_to_list[index]\
                                or "ERROR: In procedure module-lookup: Unbound variable:" in result_to_list[index]:
                            answer.append(result_to_list[index])
                        index += 1
                    self.all_answer.append(answer[-1])
                    self.all_answer.append("\n")
                    print(answer[-1])
                else:
                    self.disp.stdin.write(list_of_rules[i].encode())
                i = i + 1
        except Exception as e:
            print("Error occurred in displaying result: ", e)

    def ghostRule(self, rule):
        try:
            ruletostring = rule.decode()
            if ruletostring == '':
                pass
            elif '(ghost-parse-file' in ruletostring \
                    or '(ghost-parse' in ruletostring \
                    or '(map cog-name' in ruletostring \
                    or '(test-ghost' in ruletostring:
                self.writetofile(ruletostring)
            elif 'u:' in rule.decode() or 's:' in rule.decode():
                str = '(ghost-parse (\"{}\"))'.format(ruletostring)
                self.writetofile(str)
            else:
                action = '(map cog-name (test-ghost \"{}\"))'.format(ruletostring)
                self.writetofile(action)
        except Exception as e:
            print("Error occurred in writing rule: ", e)

    def writetofile(self, state):
        self.all_rule.append(state+"\n")
        self.question_file.write(state+"\n")
        self.displayPopen()

    def loadmodules(self):
        try:
            mod = ""
            with open('files/module.txt', 'r') as f:
                for line in f:
                    mod = mod + line
                modtobyte = mod.encode()
                self.disp.stdin.write(modtobyte)
                if self.running_times == 0:
                    print("Modules successfully loaded from file")
        except Exception as e:
            print("Error occurred in loading module from file: ", e)

    def loadrules(self, file_dir):
        try:
            instruction = ""
            with open("" + file_dir + "", 'r') as f:
                for line1 in f:
                    instruction += '(ghost-parse \"{}\")'.format(line1)
                convtobyte = instruction.encode()
                # print(convtobyte)
                self.disp.stdin.write(convtobyte)
                # self.ghostRule(convtobyte)
                if self.running_times == 0:
                    print("Rules successfully loaded from file")
        except Exception as e:
            print("Error occurred in loading module from file: ", e)

    def testguile(self):
        try:
            hello = '(ghost-parse "u: (hi robot) hello human")'
            self.disp.stdin.write(hello.encode())
            if self.running_times == 0:
                print("Guile has tested successfully!")
        except Exception as e:
            print("Error occurred in testing rule: ", e)



print("-------------Welcome-------------")
one = whole()
one.takeInput()
