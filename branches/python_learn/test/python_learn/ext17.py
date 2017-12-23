#!/usr/bin/env python3

from sys import argv
from os.path import exists

if len(argv) != 3:
    print("ARGV is Wrongful!",len(argv))
    exit
else:
    script, from_file, to_file = argv
    print("Copying from %s to %s" % (from_file,to_file))
    try:
      write_content = open(from_file)
      indata = write_content.read()
      print("The input file is %d bytes long " % len(indata))
      print("Ready,hit Retrun to continue,CTRL-C to abort.")
      input()
      output = open(to_file,'w')
      output.truncate()
      output.write(indata)
      print("Alright, all done.")
      output.close()
      write_content.close()
    except IOError:
        print("file not exists!")

