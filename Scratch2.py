# import subprocess as sp
# #
# # # p.call("ifconfig", shell=True)
# # output = p.check_output("ifconfig",shell=True).decode()
# # print(output)
#
# p = sp.Popen('guile',stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
# with open('module.txt', 'r') as f:
#     modules = ""
#     for line in f:
#         modules += line
#     tobyte = modules.encode()
#     p.stdin.write(tobyte)
#     print("Modules successfully loaded from file")
import subprocess as sp
import sys


def main():
    test_output = []
    proc = sp.Popen("guile", stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, bufsize=0)
    modules = ""
    with open('module.txt', 'r') as f:
        for line in f:
            modules += line
        proc.stdin.write(modules)
    rule = b"""(ghost-parse \"u: (hello) hi there\")"""
    proc.stdin.write(rule.decode())
    # print(proc.stdout.readline(-1))
    # for line in proc.stdout.readline():
    #     print(line)
    res1 = []
    while True:
        # if "[GHOST]" in proc.stdout.read(1):
        out1 = proc.stdout.readline()
        if out1 == '' and proc.poll() != None:
            break
        if out1 != '':
            # sys.stdout.write(out)
            res1.append(out1)
    combine = []
    for j in res1:
        # combine.append()
        if "[GHOST]" in j:
            print(j)

    # proc.stdin.write('\',q\'')
    res = []
    code = b"""(map cog-name (test-ghost "hello"))"""
    proc.stdin.write(code.decode())
    # proc.stdin.close()
    # print(proc.stdout.readline(-1))
    # for line in proc.stdout.readline():
    # print(line)
    while True:
        # if "[GHOST]" in proc.stdout.read(1):
        out = proc.stdout.readline()
        if out == '' and proc.poll() != None:
            break
        if out != '':
            # sys.stdout.write(out)
            res.append(out)
    combine = []
    for i in res:
        # combine.append()
        if "[GHOST]" in i:
            print(i)
    # print(res)
    # for line in iter(proc.stdout.readline, ''):
    #     if "[GHOST]" in line:
    #         print(line)
    # proc.stdout.close()
    # proc.wait()

    # for l in proc.communicate():
    #     if "[GHOST]" in l:
    #         test_output.append(l)
    #         # print(l)
    # print("---------")
    # print(test_output)
    # proc.kill()


main()
# for line in proc.stdout:
#     print(line)
# proc.stdin.write("ifconfig")
# proc.stdin.close()
# for line in proc.stdout:
#     print(line)
