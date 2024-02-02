from gtts import gTTS


def text_to_speech(text_input):
    language = 'en'
    sound_obj = gTTS(text=text_input, lang=language, slow=False)
    sound_obj.save("recording.mp3")



