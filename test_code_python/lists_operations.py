import sys

if __name__ == '__main__':
    e = []

    # N = [i.rstrip() for i in sys.stdin.readlines()]
    N =     [12, "insert 0 5", "insert 1 10",    "insert 0 6",    "print",    "remove 6",    "append 9",    "append 1",    "sort",    "print",    "pop",    "reverse",    "print"]
    for i in N[1:]:
        inputv = i.split(" ")
        if inputv[0] == "insert":
            e.insert(int(inputv[1]),int(inputv[2]))
        elif inputv[0] == "print":
            print(e)
        elif inputv[0] == "remove":
            e.remove(int(inputv[1]))
        elif inputv[0] == "append":
            e.append(int(inputv[1]))
        elif inputv[0] == "sort":
            e.sort()
        elif inputv[0] == "pop":
            e.pop(-1)
        elif inputv[0] == "reverse":
            e.reverse()
