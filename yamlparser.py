#!/usr/bin/env python3
import yaml
import sys

if len(sys.argv) != 2:
  print('Usage: yamlparser.py <filename>')
  sys.exit(1)

try:
  #print('opening ' + sys.argv[1])
  with open(sys.argv[1], 'r') as f:
    yaml.load(f)
except OSError as oe:
  print(oe)
  sys.exit(1)
except Exception as e:
  #print(type(e))
  print(e)
  sys.exit(1)

sys.exit()

