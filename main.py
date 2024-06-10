import pyttsx3

Robo = pyttsx3.init()
print("welcome")
while(True):
    user_input= input("enter speak (0 to exit): ")
    if user_input=="0":
        break
    else:
        print(user_input)
        Robo.say(user_input)
        Robo.runAndWait()




