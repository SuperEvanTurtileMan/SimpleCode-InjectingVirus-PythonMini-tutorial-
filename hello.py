#!/usr/bin/env python

usrname = input("Please enter in your username ")
pwd = input("Please enter in your password ")
pay = 0

if usrname.lower() == "turtile":
    if pwd.lower() == "asdfasdf":
        print("Hello user " + usrname)
        pay = 1000000
        print("You have a pay of $", pay, " in your account")
    else:
        print("Incorrect password")
else:
    print("Not an existing user")