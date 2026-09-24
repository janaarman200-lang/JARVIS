class VoiceSpeaker:
    def speak(self, text: str) -> None:
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except ImportError:
            raise RuntimeError("Install optional voice dependencies first.")
