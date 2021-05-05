#fh=open("/etc/passwd","r")
import sys
fh = sys.stdin
for line in fh:
    line=line.strip()
    userdb=line.split(":")
    uid=userdb[2]
    shell=userdb[6]
    if int(uid) <= 1000 and shell == "/bin/bash":
        print(line)
fh.close()
