import subprocess as sp

class whole:
    def __init__(self):
        self.all_rule = []
        self.all_answer = []
        self.running_times = 0
        self.question_file = open("files/cache.txt", "a+")

    def takeInput(self):
        self.displayPopen()
        while True:
            self.running_times = self.running_times + 1
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
        disp = sp.Popen('guile', stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
        try:
            a = disp.stdout.readline()
            if "GNU Guile" in a.decode():
                if self.running_times == 0:
                    print("guile successfully opened")
            else:
                print("there is a problem with guile")
        except Exception as e:
            print("Error occurred in starting guile: ", e)

        try:
            mod = ""
            with open('files/module.txt', 'r') as f:
                for line in f:
                    mod = mod + line
                modtobyte = mod.encode()
                disp.stdin.write(modtobyte)
                if self.running_times == 0:
                    print("Modules successfully loaded from file")
        except Exception as e:
            print("Error occurred in loading module from file: ", e)
        try:
            hello = '(ghost-parse "u: (hi robot) hello human")'
            disp.stdin.write(hello.encode())
            if self.running_times == 0:
                print("guile tested successfully")
        except Exception as e:
            print("Error occurred in testing rule: ", e)

        list_of_rules = self.all_rule
        aa = len(list_of_rules)
        try:
            i = 0
            while i <= aa - 2:
                if i == aa - 2:
                    stdou, stder = disp.communicate(input=list_of_rules[aa - 2].encode())
                    result_to_list = stdou.decode().split('\n')

                    answer = []
                    index = 0
                    while index < len(result_to_list):
                        if "[GHOST]" in result_to_list[index] \
                                or "<unnamed port>" in result_to_list[index] \
                                or "<unspecified>" in result_to_list[index] \
                                or "ERROR: In procedure module-lookup: Unbound variable:" in result_to_list[index]:
                            answer.append(result_to_list[index])
                        index += 1
                    self.all_answer.append(answer[-1])
                    self.all_answer.append("\n")
                    print(self.all_answer[-2])
                else:
                    disp.stdin.write(list_of_rules[i].encode())
                i = i + 1
        except Exception as e:
            print("Error occurred in displaying result: ", e)

    def ghostRule(self, rule):
        try:
            ruletostring = rule.decode()
            if ruletostring == '':
                pass
            elif '(ghost-parse-file' in ruletostring \
                    or '(ghost-parse' in ruletostring:
                self.all_rule.append(ruletostring)
                self.all_rule.append("\n")
                self.question_file.write(ruletostring)
                self.question_file.write('\n')
                self.displayPopen()
            elif 'u:' in rule.decode() or 's:' in rule.decode():
                str = '(ghost-parse (\"{}\"))'.format(ruletostring)
                self.all_rule.append(str)
                self.all_rule.append("\n")
                self.question_file.write(str)
                self.question_file.write('\n')
                self.displayPopen()
            else:
                action = '(map cog-name (test-ghost \"{}\"))'.format(ruletostring)
                self.all_rule.append(action)
                self.all_rule.append("\n")
                self.question_file.write(action)
                self.question_file.write('\n')
                self.displayPopen()

        except Exception as e:
            print("Error occurred in writing rule: ", e)


print("-------------Welcome-------------")
one = whole()
one.takeInput()
