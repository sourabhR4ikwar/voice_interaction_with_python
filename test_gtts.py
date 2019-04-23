import os
from playsound import playsound
from gtts import gTTS


def speak(text, count):
    voice = gTTS(text=text,lang="hi",slow=False)
    voice.save("tempText2speech"+str(count)+".mp3")
    playsound("tempText2speech"+str(count)+".mp3")
    os.remove("tempText2speech"+str(count)+".mp3")


text = ""
count = 0
while text != "bye":
    print("Write something you want me to say.")
    print(" >> ",end="")
    text = input();
    print("Processing Text...")
    speak(text, count)
    count = count + 1
