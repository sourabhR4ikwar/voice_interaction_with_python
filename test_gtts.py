import os
from gtts import gTTS as speak

text = "hey sourabh";

voice = speak(text=text,lang="en",slow=False)
voice.save("sample.mp3")

os.system("mpg321 sample.mp3")
