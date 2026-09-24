class VoiceListener:
    def listen(self) -> str:
        try:
            import speech_recognition as sr
        except ImportError:
            raise RuntimeError("Install optional voice dependencies first.")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)
