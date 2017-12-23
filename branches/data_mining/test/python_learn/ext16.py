#!/usr/bin/env python3

from sys import argv
if len(argv) != 2 :
    print("ARGV is Wrongful!",len(argv))
    exit
else:
  script,filename = argv
  print("We're going to erase %r." % filename)
  print("If you don't want that,hit CTRL-C(^C).")
  print("If you do want that, hit RETURN.")
  input("?")
  print("Opening the file...")
  target = open(filename,'w')
  print("Truncating the file.Goodbye!")
  target.truncate()
  print("Now I'm going to ask for three lines.")
  line1 = input("line 1:")
  line2 = input("line 2:")
  line3 = input("line 3:")
  print("I'm going to write there to the file")
  target.write(line1)
  target.write("\n")
  target.write(line2)
  target.write("\n")
  target.write(line3)
  target.write('\n')

  print("And finally,we close it.")
  target.close()
  try:
      wrifile = open(filename,'r')
      file_con = wrifile.read()
      print("文件内容:")
      print(file_con)
  except IOError:
      print("no file exists！",filename)