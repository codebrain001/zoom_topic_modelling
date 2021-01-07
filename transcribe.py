import time
# Imports the Google Cloud client library
from google.cloud import speech
# Import the google service account api authentication
from google.oauth2 import service_account


class AudioTranscriber:
    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_file(
            'key.json')
        self.client = speech.SpeechClient(credentials=self.credentials)
        # Audio file to be transcribed from google cloud bucket
        self.gcs_uri = "gs://zoom_project_data/audio.flac"
        self.audio = speech.RecognitionAudio(uri=self.gcs_uri)

    def transcribe(self, language_code):
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            language_code=language_code,
            # audioChannelCount=channel_count,
            # enableSeparateRecognitionPerChannel=True,
        )

        transcript = ''

        # Detects speech in the audio file
        operation = self.client.long_running_recognize(
            config=config, audio=self.audio)
        start_time = time.time()
        print("Waiting for operation to complete...")
        response = operation.result()

        for result in response.results:
            transcript += result.alternatives[0].transcript

        print(f'Transcription took {time.time()-start_time}seconds')
        return transcript


zoom_project = AudioTranscriber()
transcript = zoom_project.transcribe("en-US")
print(transcript)
