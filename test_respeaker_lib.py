import time
from respeaker import Microphone


def main():
    mic = Microphone()
    while True:
        if mic.wakeup("bravo"):
            print("Wake word detected")
            audio_data = mic.listen()
            text = mic.recognize(audio_data)
            if text:
                print("Recognized:", text)


if __name__ == "__main__":
    main()
