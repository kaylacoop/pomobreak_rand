print ("Congrats on finishing your work session, Ready for break randomization?")
print ("Here are the break genre options:")
print (" ")
print ("a) Health Boost")
print ("b) Brain Boost")
print ("c) Creative Boost")
print (" ")
break_des = input("a, b, c?     ")       

alist = ["Deep Breathing Box Method","Strech Out","Rehydrate Intentionally","Lymphatic Pressure Points Stress Relief","Gratitude for what this pomo will contribute in your future"]
blist = ["Chess Puzzles","Typing Test","Quick Maths Game","Wordle","Speedrun Sudoku"]
clist = ["Quick Sketches 30s","Quick Sketches 2m","Song & Doodle","Photoshop Daily Challenge", "Flowchart of Making Tea"]

import random as r
numpicker = r.randint(0,4)

print (" ")
if break_des == ("a"):
    print ("For your Health Boost Break try out...")
    print (alist[numpicker])
if break_des == ("b"):
    print ("For your Brain Boost Break try out...")
    print (blist[numpicker])
if break_des == ("c"):
    print ("For your Creative Boost Break try out...")
    print (clist[numpicker])

print ("Come back after your next work session. Keep it up!")
