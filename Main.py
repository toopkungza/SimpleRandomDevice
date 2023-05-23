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

stastified = "n"
ready = input("Are you ready to let me decide whatever in your mind right now? (Y/n) \n").lower()
randomcounter = []

if ready == "y":
    while stastified == "n":  
        randomx = random.random()
        if randomx > 0.5:
            print("Yes/Left/Go forward/Switch to the other/1 \n")
            randomcounter.append(1)
        else:
            print("No/Right/Stop/Stay the same/0 \n")
            randomcounter.append(0)
        stastified = input("Stastified? (y/n) \n").lower()
        if stastified == "y":
            print("Total times I ran: ", len(randomcounter))
            print("Total counts for Yes/1: ", randomcounter.count(1))
            print("Total counts for No/0: ", randomcounter.count(0))            
            print("Have a nice day! Goodbye.")
        else:
            stastified = "n"
if ready == "n":
    print("Bye! :)")
