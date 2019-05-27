#!/usr/bin/python3

import subprocess
import sys

argci = 1
args = ["git"]

def cmp():
  return sys.argv[argci].lower()

mappings = {
  "uchiha": "clone",
  "7/23": "init",
  "kunai": "add",
  "choke": "rm",
  "speed": "mv",
  "sharingan": "pull"
}

def map(cmd):
  if cmd[0] in mappings:
    return mappings[cmd[0]]
  elif cmd[0] == "vs":
    if cmd[1] == "itachi":
      return "commit"
    elif cmd[1] == "naruto":
      return "push"
    else:
      print("sasuke.py: bad option")
      sys.exit(1)
  else:
    print("sasuke.py: bad option")
    sys.exit(1)

# map the action (but check if no options were provided)
if len(sys.argv) == 1:
  proc = subprocess.run(args);
  sys.exit(proc.returncode)
mapped = ""
if cmp() == "vs":
  argci += 1
  mapped = map(["vs", cmp()])
else:
  mapped = map([cmp()])
args.append(mapped)
argci += 1

# pipe the rest of argv
args.extend(sys.argv[argci:])

# print command we are about to run then run
print("sasuke.py: " + " ".join(args))
proc = subprocess.run(args)
sys.exit(proc.returncode)
