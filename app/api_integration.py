from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
import requests
import os
from . import settings  # Import your settings

# Initialize Google Cloud clients
translate_client = translate.Client()
tts_client = texttospeech.TextToSpeechClient()

def handle_translation(text, target_language):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def handle_tts(text, language_code):
    """Handles Google Cloud Text-to-Speech."""
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code=f'{language_code}-IN')
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    import uuid
    voiceover_filename = f'voiceover_{str(uuid.uuid4())}.mp3'
    output_path = os.path.join('static', 'audio', voiceover_filename)

    with open(output_path, 'wb') as out:
        out.write(response.audio_content)

    return output_path  # Return the file path

def handle_sarvam_tts(text, language_code):
    """Generates a voiceover using Sarvam's TTS API."""

    url = "https://api.sarvam.ai/tts/v1/generate"
    headers = {
        "Authorization": f"Bearer {settings.SARVAM_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "language": language_code,
        "voice_id": "your-chosen-voice-id"  # Replace with desired voice ID
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        audio_data = response.content

        import uuid
        filename = f"sarvam_voiceover_{str(uuid.uuid4())}.mp3"
        output_path = os.path.join('static', 'audio', filename)

        with open(output_path, 'wb') as f:
            f.write(audio_data)

        return output_path
    else:
        print(f"Sarvam TTS API Error: {response.status_code} - {response.text}")
        return None  # Or raise an exception
