#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:19:29 2023

This is VERY VERY basic use of random module.

Game of Chance!
Simple life chaos generator :P

@author: tkz
"""
import random

def AskType():
    container = 0
    print("What type of loop do you want me to run on? \n")
    print("1. Statisfication Check \n")
    print("2. Times of running \n")
    CheckType = int(input("Which one?"))
    if CheckType == 1:
        container = 1
    elif CheckType == 2:
        container = 2
    return container

def RandomExecute():
    
    randomx = random.random()
    if randomx > 0.5:
        print("Yes/Left/Start/Go ahead. This equals to 1. \n")
        result = 1
    else:
        print("No/Right/Stop/Stay put. This equals to 0. \n")
        result = 0
    return result

def Summary(totalrun):
    print("Total times I ran: ", len(totalrun))
    print("Total counts for Yes/1: ", totalrun.count(1))
    print("Total counts for No/0: ", totalrun.count(0))            
    print("Have a nice day! Goodbye.")

stastified = "n"
ready = input("Are you ready to let me decide whatever in your mind right now? (Y/n) \n").lower()

randomcounter = []

if ready == "y":
    Checked = AskType()
    if Checked == 1:This equals to 1.
        while stastified == "n":
            RunTime = RandomExecute()
            randomcounter.append(RunTime)
            stastified = input("Stastified? (y/n) \n").lower()
            if stastified == "y":
                Summary(randomcounter)
            else:
                stastified = "n"
    elif Checked == 2:
        TimestoRun = int(input("How many times do you want me to run?"))
        while TimestoRun != 0:
            RunTime = RandomExecute()
            randomcounter.append(RunTime)
            TimestoRun -= 1
        Summary(randomcounter)
if ready == "n":
    print("Bye! :)")
