#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:19:29 2023

This is VERY VERY basic use of the random module with interesting features... :P

Game of chance is pretty much like the game of life!
- Simple life chaos generator

@author: tkz

TEST20240222
"""
import random

#777 digits
def GetRandomPiSeq(desireddigits):    
    pidigits = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297805"
    selecteddigits = "0"
    while selecteddigits[0] == "0": #to prevent the start of 0 in digits, which results in only 4 sequences 
        startindex = random.randint(0, (len(pidigits)-(desireddigits)))
        selecteddigits = pidigits[startindex:(startindex+desireddigits)]
    return selecteddigits

def AskType():
    print("What type of loop do you want me to run on? \n")
    print("1. Statisfication Check \n")
    print("2. Times of running \n")
    print("3. Run based on the total times of the 5 sequences randomly selected from any of 777 decimal points of pi (eg. 14159 or 97932 or 97494). \n")
    CheckType = int(input("Which one (1-3)? \n"))
    return CheckType

def RandomExecute():
    print("Generating...")
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

if __name__ == "__main__":
    ready = input("Are you ready to let me decide what's in your mind right now? (Y/n) \n").lower()
    randomcounter = []
    if ready == "y":
        Checked = AskType()
        if Checked == 1:
            SatisfiedCheck = False
            while SatisfiedCheck == False:
                RunTime = RandomExecute()
                randomcounter.append(RunTime)
                SatisfiedCheck = input("Satisfied? (y/n) \n").lower()
                if SatisfiedCheck == "y":
                    SatisfiedCheck = True
                    Summary(randomcounter)
                else:
                    SatisfiedCheck = False
        elif Checked == 2:
            TimestoRun = int(input("How many times do you want me to run? \n"))
            while TimestoRun != 0:
                RunTime = RandomExecute()
                randomcounter.append(RunTime)
                TimestoRun -= 1
            Summary(randomcounter)
        elif Checked == 3:
            randompi = GetRandomPiSeq(5)
            TimestoRun = int(randompi)
            while TimestoRun != 0:
                RunTime = RandomExecute()
                randomcounter.append(RunTime)
                TimestoRun -= 1
            Summary(randomcounter)
    if ready == "n":
        print("Bye! :)")
