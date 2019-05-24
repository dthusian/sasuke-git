#!/usr/bin/python3

import subprocess
import sys

argci = 1
args = ["git"]

def cmp():
  return sys.argv[argci].lower()

def map(cmd):
  if cmd[0] == "uchiha":
    return "clone"
  elif cmd[0] == "kunai":
    return "add"
  elif cmd[0] == "choke":
    return "rm"
  elif cmd[0] == "vs":
    if cmd[1] == "itachi":
      return "commit"
    elif cmd[1] == "naruto":
      return "push"

# map the action
mapped = ""
if cmp() == "vs":
  argci += 1
  mapped = map(["vs", cmp()])
else:
  mapped = map([cmp()])
args.append(mapped)
argci += 1

# pipe the rest of argv
for i in range(argci, len(sys.argv)):
  args.append(sys.argv[i])

# print command we are about to run then run
print(" ".join(args))
subprocess.run(args)
