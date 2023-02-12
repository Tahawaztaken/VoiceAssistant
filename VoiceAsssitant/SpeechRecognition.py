import speech_recognition, time

recognizer = speech_recognition.Recognizer()

text_list = {"Command" : "Null"}


def transcribe_audio():
    try:
          
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            text_list["Command"] = text
            return text_list
    except speech_recognition.UnknownValueError:
        return {"Command": "Nothing"}


# while True:
#       choice = input("Anotha one?(y/n) ")
#       if choice == 'y':
#             transcribe_audio()
#       else:
#         print("see ya")
#         break


print(text_list)
