
"""
Created on Wed Sep 11 19:25:38 2019

@author: Mahender jakhar

"""
#google text to speech
from gtts import gTTS

# os library provides functions to interact with the OPERATING SYSTEM
import os

#myText = " Hello my name is mahender jakhar and this is my first python script "

mj = open("mjsample.txt",'r')
myText = mj.read()
language = 'en'
output = gTTS(text = myText,lang = language,slow  = False )
output.save("mj_output.mp4")
mj.close()
os.system("start mj_output.mp4")
