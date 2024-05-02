import speech_recognition as sr
from pyfirmata import Arduino, SERVO, util
from time import sleep
from rr import round_robin
from fff import fcfs_scheduling


def change(numbersid):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    with mic as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = r.listen(source)
                command = r.recognize_google(audio).lower()  # Convert to lowercase for case-insensitive matching
                if command in ("round robin", "rr"):
                    if len(numbersid) >=4:
                        print("Sending numbers list to change function (length exceeds 4).")
                        print(round_robin(numbersid,2))
                    else:
                        print("now")
                if command in("fcfs","first come first serve"):
                    print("Sending numbers list to change function (length exceeds 4).5454")
                    print(fcfs_scheduling(numbersid))

                else:
                    print("blabla")
            except sr.UnknownValueError:
                print("Audio could not be understood")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


