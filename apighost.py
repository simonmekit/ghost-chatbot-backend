import subprocess as sp
import os
import sys


class whole:
    def __init__(self):
        self.isGuile = False
        self.takeInput()
        self.proc = ""

    def takeInput(self):
        self.startGuile()
        value = input("Please enter your rule or '(quit)' to exit: ")
        if value == "(quit)":
            found = input("Are you sure? Y or N: ")
            if found == "Y" or found == "y":
                raise SystemExit
            else:
                self.takeInput()
        self.ghostRule(value.encode())

    # def startRelex(self):
    #     if not self.isRelex:
    #         print("----------opening relex server------------")
    #         try:
    #             os.chdir("/home/brook/Documents/relex/")
    #             os.system("gnome-terminal -e 'bash -c \"./opencog-server.sh; exec bash\"'")
    #             print("Relex Server opened successfully")
    #             self.isRelex = True
    #             self.takeInput()
    #         except Exception as e:
    #             self.isRelex = False
    #             print("Error occured in opening relex server")
    #             exit(0)

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

    # def displayPopen(self):
    # 	disp = sp.Popen('guile', stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
    # 	try:
    # 		a = disp.stdout.readline()
    # 		if("GNU Guile" in a.decode()):
    # 			pass
    # 		else:
    # 			print("there is a problem with guile")
    # 	except Exception as e:
    # 		print("Error Occured in starting guile: ", e)
    # 	try:
    # 		module = b"""
    # 					(use-modules(opencog)
    # 					(opencog nlp)
    # 					(opencog nlp relex2logic)
    # 					(opencog openpsi)
    # 					(opencog ghost)
    # 					(opencog ghost procedures))"""
    # 		disp.stdin.write(module)
    # 		# print(type(h))
    # 		#print("Modules suc	cessfully loaded")
    # 	except Exception as e:
    # 		# print("problem occured while trying to load modules ")
    # 		print("Error Occured in loading module: ", e)
    #
    # 	try:
    # 		code = b"""
    # 				(ghost-parse "u: (hello) hi there")
    # 				"""
    # 		disp.stdin.write(code)
    # 		#print(self.proc.stdout())
    # 		test = b"""
    # 				(map cog-name (test-ghost "hello"))
    # 				"""
    # 		disp.stdin.write(test)
    #
    # 	except Exception as e:
    # 		print("Error Occured in testing rule: ", e)
    #
    #
    # 	# spliting all the given rule into objects of list
    # 	list_of_rules = self.all_rule.split('\n')
    # 	aa = len(list_of_rules)
    # 	try:
    # 		i = 0
    # 		# its aa-2 because the last elt f[aa-1] is New line('\n') so the last input or current input asked
    # 		# by user is found on f[aa-2]
    # 		while(i <= aa-2):
    # 			# if the rule is the last rule or the current rule that user expecting its answer
    # 			# to display its answer
    # 			if(i == aa-2):
    # 				# extracting the output and error of the current rule asked by user
    # 				stdou, stder = disp.communicate(input=list_of_rules[aa - 2].encode())
    #
    # 				# first changing stdou output into string then split it with '\n'
    # 				self.out = stdou.decode().split('\n')
    # 				# when you enter a rule and want to display with communicate it didnot display only what you need
    # 				# it displays all previous output together so how can you avoid this
    # 				#print(stdou)
    #
    # 				# so to display only the short breif answer to user by removing the Error and other
    # 				# bu the problem of this is all the output displayed by every ghost rule is not belongs to only this
    # 				# five group of categories
    # 				j = 0
    # 				current_answer = []
    # 				while(j < len(self.out)):
    # 					if("[INFO] [GHOST] Say:" in self.out[j]) \
    # 							or ("[WARN] [GHOST]" in self.out[j]) \
    # 							or ("<unnamed port>" in self.out[j]) \
    # 							or ("<unspecified>" in self.out[j]) \
    # 							or ("ERROR: In procedure module-lookup: Unbound variable:" in self.out[j]):
    # 						#print(self.out[i])
    # 						current_answer.append(self.out[j])
    # 					else:
    # 						pass
    # 					j = j+1
    #
    # 				# now check that whether the output from guile is statement or empty string
    # 				# because if its empty then displaying empty string to user as guile
    # 				# if its statement display this statement to user
    # 				#print("length of self.out", len(self.out))
    # 				# add the length of the output displayed from guile to length of output from guile
    # 				self.len_of_output_from_guile.append(len(self.out))
    # 				# if the output from guile is empty then it is increased by 1 from previous length
    # 				# but if its not empty its increased by 7, we checked it many times
    # 				# so append empty string to all answer if output is empty other wise append the output from guile
    # 				# we go through all this process because if the output from guile is empty it couldnot display this empyt
    # 				# output to us
    # 				if ((self.len_of_output_from_guile[len(self.len_of_output_from_guile) - 1] - self.len_of_output_from_guile[
    # 					len(self.len_of_output_from_guile) - 2]) == 1):
    # 					self.all_answer.append(" ")
    # 				else:
    # 					self.all_answer.append(current_answer[len(current_answer) - 1])
    #
    # 				# then display the last output to user which is corresponding to the current asked rule
    # 				print(self.all_answer[len(self.all_answer) - 1])
    #
    # 				# # so from the list of a bunch of output display only the last elt of the list which is most probably
    # 				# # corresponds to the output of the current rule asked by user
    # 				# print("len of list of rules", len(list_of_rules))
    # 				# print(list_of_rules)
    # 				# print("\n")
    # 				#
    # 				# print("len of output", len(current_answer))
    # 				# print(current_answer)
    # 				# print("\n")
    # 				# #print(output[len(output)-1])
    # 				#
    # 				# print("len of all_answer", len(self.all_answer))
    # 				# print(self.all_answer)
    # 				# print("\n")
    # 				# # # print("self.index", self.empty_index)
    # 				# # # print("\n")
    #
    # 			# if the rule is all the previous rule asked by the user
    # 			# this is only just to write
    # 			else:
    # 				disp.stdin.write(list_of_rules[i].encode())
    #
    # 			i = i+1
    # 	except Exception as e:
    # 		print("error occured in writing rule", e)

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
            # print(self.proc.communicate())
        except Exception as e:
            print("Error Occured in testing rule: ", e)

    def ghostRule(self, rule):
        try:
            toString = rule.decode()

            if 'ghost-parse-file' in toString or 'ghost-parse' in toString:
                self.proc.stdin.write(toString)
                return self.proc.stdout.readline()
            elif toString != '':
                rule = '(map cog-name (test-ghost \"{}\"))'.format(toString)
                self.proc.stdin.write(rule)
                return self.proc.stdout.readline()
            elif toString == '':
                self.takeInput()
        # communicating the input with the sheme guile process
        # the great problem i faced is cannot send input after starting communication
        # c = self.proc.communicate(input=rule)
        # ss = self.proc.stdout
        # print(ss)
        # output = self.displayPopen(ss)
        # print(output)
        # self.proc.poll()
        # stdout, stderr = self.proc.communicate(input=rule)
        # displaying only the required information from the bunch of outptu line
        # first decoding byte into string then spliting with newline then displaying the second line
        # out = stdout.decode().split('\n')
        # print(out[1])
        # self.proc.wait()
        # self.nProc = self.newPopen(ss)

        # stdout = []
        # while True:
        # 	line = self.proc.stdout.readline()
        # 	stdout.append(line),
        # 	if line == '':
        # 		break
        # print(stdout)

        # for line in iter(self.proc.stdout.readline, ''):
        # 	print(line.rstrip())

        #
        # while True:
        # 	line = self.proc.stdout.readline()
        # 	if(line != b''):
        # 		os.write(1, line)
        # 	else:
        # 		break

        # b = proc.stdout.readline()
        # print(b)

        # r = b"""
        #   		(map cog-name (test-ghost "brook"))
        #   		"""
        # proc.stdin.write(r)
        except Exception as e:
            print("Error Occured in writing rule: ", e)


print("-------------Welcome-------------")
one = whole()
