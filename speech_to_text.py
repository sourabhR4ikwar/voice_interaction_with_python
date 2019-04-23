import speech_recognition as sr

recognizer = sr.Recognizer();
with sr.Microphone() as source:
    print("say something : ")
    audio = recognizer.listen(source)
    print("Time over Thanks")


try:
    print("Text : "+recognizer.recognize_google(audio))
except:
    pass
