import pyttsx3
robot_mouth = pyttsx3.init()

"""VOICE"""
voices = robot_mouth.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
robot_mouth.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

robot_brain = "Hello my Boss"

robot_mouth.say(robot_brain)
robot_mouth.runAndWait()