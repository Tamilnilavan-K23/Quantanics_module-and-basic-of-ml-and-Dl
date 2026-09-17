import pyttsx3

engine=pyttsx3.init()
engine.say("hello,how are you")
engine.runAndWait()

rate=engine.setProperty('rate')
engine.getproperty('rate',150)

voice=engine.setProperty('voice')