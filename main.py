from gtts import gTTS
from pydub import AudioSegment

def tts(text, language, gender, output_file):
    # Determine the language and gender-specific language code
    language_codes = {
        'English': 'en',
        'Spanish': 'es',
    }

    voices = {
        'British Male': 'en-uk',
        'American Male': 'en-us',
        'British Female': 'en-uk',
        'American Female': 'en-us',
        'Spanish Male': 'es-mx',
        'Spanish Female': 'es-es',
    }

    lang_code = language_codes.get(language, 'en')
    voice_code = voices.get(gender, 'en-us')

    # Create the gTTS object
    tts_obj = gTTS(text, lang=lang_code, slow=False, lang_check=False)

    # Save the audio as .mp3
    tts_obj.save("temp.mp3")

    # Load the .mp3 and export it as .wav
    audio = AudioSegment.from_mp3("temp.mp3")
    audio.export(output_file, format="wav")

if __name__ == "__main__":
    text = input("Enter the text: ")
    language = input("Enter the language (English/Spanish): ")
    gender = input("Enter the voice (British Male/American Male/British Female/American Female/Spanish Male/Spanish Female): ")
    output_file = input("Enter the output filename (e.g., output.wav): ")

    tts(text, language, gender, output_file)
