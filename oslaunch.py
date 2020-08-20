import os
import pyttsx3

print(" To Know My Services Ask Me Anay Way  ")
pyttsx3.speak(" to know my services ask me anay way ")


while True:
 pyttsx3.speak("what can i do for you  ")
 p = input(" what can i do for you :  ")
	
	
 if(("open" in p)or("run" in p)or("start" in p))and("strug" in p) and ("chrome"in p):
    os.system("start chrome")
    pyttsx3.speak(" chrome is launched")

 elif(("open" in p)or("run" in p)or("show" in p)) and ("services"in p):
    print("welcome to my services ")
    pyttsx3.speak("welcome to my services ")
    print(" #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||# \n")
    print("you can use chrome from here ")
    pyttsx3.speak("you can use chrome from here")
    print("you can use google meet from here")
    pyttsx3.speak("you can use google meet from here ")
    print("you can use notepad  from here ")
    pyttsx3.speak("you can use notepad  from here ")
    print("you can use facebook from here ")
    pyttsx3.speak("you can use facebook from here ")
    print("you can use gmail from here")
    pyttsx3.speak("you can use gmail from here ")
    print("you can use google maps  from here")
    pyttsx3.speak(" you can use google maps  from here")
    print("you can play your favourite song from here")
    pyttsx3.speak(" you can play your favourite song from here ")
    print("you can use whatshapp from here \n")
    pyttsx3.speak(" you can use whatshapp from here")
    pyttsx3.speak(" these are my services ")

 elif(("show" in p)or("write" in p)or("your" in p)) and ("name"in p):
    print("Hello I Am STRUG ")
    pyttsx3.speak("Hello I Am STRUG")

 elif(("open" in p)or("run" in p)or("start" in p)) and("notepad"in p):
    os.system("notepad")
    pyttsx3.speak(" notepad is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and ("facebook"in p):
    os.system("start chrome facebook.com")
    pyttsx3.speak("facebook is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and (("whatsapp" in p)or("whatsapp web"in p)):
    os.system("start chrome web.whatsapp.com")
    pyttsx3.speak("whatsapp is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and ("youtube"in p):
    os.system("start chrome youtube.com")
    pyttsx3.speak("youtube is launched")

 elif(("open" in p)or("start" in p)) and ("gmail"in p):
    os.system("start chrome gmail.com")
    pyttsx3.speak("your gmail is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and ("googlemeet"in p):
    os.system("start chrome meet.google.com")
    pyttsx3.speak("googlemeet is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and (("googlemap" in p)or("google map"in p)):
    os.system("start chrome https://www.google.com/maps/@26.8959744,75.7792768,12z ")
    pyttsx3.speak("google map is launched")

 elif(("open" in p)or("play" in p)or("run" in p)or("start" in p)) and (("favourite song")or("favourite"in p)):
    os.system("start chrome https://www.youtube.com/watch?v=cl0a3i2wFcc")
    pyttsx3.speak("injoy your favourite song ")

 elif("exit" in p):
    print(" THANKS FOR USING MY SERVICES   😊 😊 😊 😊 😊 ")
    pyttsx3.speak("   THANKS FOR USING MY SERVICES   ")
    break
 else:	
    print("not valid")
    pyttsx3.speak("not valid service")


