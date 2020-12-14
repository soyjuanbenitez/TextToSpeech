import pyttsx3

engine = pyttsx3.init()

message = input("Write what you want here: ")

engine.say(message)
engine.runAndWait()