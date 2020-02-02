from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
from playsound import playsound
# The text that you want to convert to audio 
mytext = 'Zhaowen Ding, Zhaowen Ding, Zhaowen Ding'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
  
# Playing the converted file 
playsound("welcome.mp3")