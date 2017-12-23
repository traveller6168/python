#!/usr/bin/env python3
from sys import argv
script,first,second,third = argv
print("THE script is called:",script,
      "\nYour first variable is:",first,
      "\nYour second variable is:",second,
      "\nYour third variable is:",third
      )

tmp_argv = argv
script_name,user_name = argv[0],argv[1]
prompt = '>'
print("Hi %s,I'm the %s script." % (user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s" % user_name)
likes = input(prompt)
print("Where do you live %s?" % user_name)
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("""
         Alright,so you said %r about like me.
         You live in %r,not sure where that is.
         And you have a %r computer.Nice.
       """ % (likes,lives,computer))