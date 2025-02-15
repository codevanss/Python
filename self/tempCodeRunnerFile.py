
with open("self/output.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 4
    print(lines[3])