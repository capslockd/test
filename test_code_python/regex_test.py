# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

def main(eid):
    valid = 0
    if len(eid) != 10:
        valid = 1
    
    for j in eid:
        if eid.count(j) > 1:
            valid = 2
                    
    x = re.findall('[A-Z]',eid)
    if len(x) <= 2:
        valid = 3
        
    y = re.findall('[0-9]',eid)
    if len(y) < 3:
        valid = 4

    z = re.findall('\W',eid)
    if len(z) != 0:
        valid = 5
        
    if valid != 0:
        print(f"Invalid")
    else:
        print(f"Valid")
    
if __name__ == '__main__':
    eid = [i.rstrip() for i in sys.stdin.readlines()]
    items = int(eid[0])
    for i in range(items):
        main(eid[i+1])