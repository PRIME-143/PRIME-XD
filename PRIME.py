import os,sys
os.system("git pull")
try:
    __import__("PRIME").prime()
except Exception as e:
    exit(str(e))
