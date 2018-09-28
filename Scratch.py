#
# import subprocess as sp
# import sys
# p = ""
# def main():
#     p = sp.Popen('guile', stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
#     try:
#         a = p.stdout.readline()
#         if "GNU Guile" in a.decode():
#             print("Guile successfully opened")
#         else:
#             print("Guile Failed!")
#             exit(0)
#         try:
#             modules = ""
#             with open('module.txt', 'r') as f:
#                 for line in f:
#                     modules += line
#                 tobyte = modules.encode()
#                 p.stdin.write(tobyte)
#                 print("Modules successfully loaded from file")
#         except Exception as e:
#             print("Error occurred while trying to load modules from file: ", e)
#     except Exception as e:
#         print("Error occurred in starting guile: ", e)
#
#
#     print("--------------------GUILE has Started----------------------")
#     code = b"""(ghost-parse \"u: (hello) hi there\")"""
#     print("---1--")
#     # p.stdin.write(code.encode())
#     sp.check_output(code,shell=True)
#     print("---2--")
#
#     # print(p.stdout.readline())
#     eshi = (p.stdin.readlines().decode())
#     print(eshi)
#     print("---3--")
#     # p.stdin.write(code)
#     # print("Checking 2")
#     # outout = p.stdout.read(1)
#     # p.stdout.write(outout.decode())
#     # print("Checking 3")
#
#     test = b"""
#             (map cog-name(test-ghost "hello"))
#             """
#     # print(p.communicate())
#     p.stdin.write(test)
#
#     while True:
#         out = p.stdout.read(1)
#         if out == '' and p.poll() != None:
#             break
#         if out != '':
#             sys.stdout.write(out.decode())
#             # sys.stdout.flush()
# main()