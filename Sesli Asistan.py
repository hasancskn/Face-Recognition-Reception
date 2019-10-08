import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Sohbet edelim!")
    audio = r.listen(source)

try:

    print(r.recognize_google(audio)+"Diyorsun")
except sr.UnknownValueError:
    print("Sesini anlayamadım")
except sr.RequestError as e:
    print("Sonuç istenmedi; {0}".format(e))