
# Text-to-Speech App

This is a simple Python application for converting text to speech and saving it as a .wav audio file. The app allows you to choose from different languages and voices.

## Prerequisites

Before running the app, make sure you have the following libraries installed:

- [gTTS](https://pypi.org/project/gTTS/): For text-to-speech conversion.
- [PyDub](https://pypi.org/project/pydub/): For working with audio files.

You can install them using pip:

```
pip install gTTS pydub
```

## Usage

1. Run the `tts_app.py` script using Python.

   ```bash
   python tts_app.py
   ```

2. The app will prompt you for the following information:
   - Enter the text you want to convert to speech.
   - Choose the language (English/Spanish).
   - Select the voice (British Male/American Male/British Female/American Female/Spanish Male/Spanish Female).
   - Enter the output filename (e.g., output.wav).

3. The app will generate the audio file in .wav format with the selected language and voice.

## Example

Here's an example usage of the app:

```plaintext
Enter the text: Hello, this is a test.
Enter the language (English/Spanish): English
Enter the voice (British Male/American Male/British Female/American Female/Spanish Male/Spanish Female): American Male
Enter the output filename (e.g., output.wav): output.wav
```

The generated audio file (`output.wav`) will contain the speech based on your input.

Enjoy using the Text-to-Speech App!
```
