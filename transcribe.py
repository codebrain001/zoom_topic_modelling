import time
# Imports the Google Cloud client library
from google.cloud import speech
# Import the google service account api authentication
from google.oauth2 import service_account


class AudioTranscriber:
    def __init__(self,URI):
        self.credentials = service_account.Credentials.from_service_account_file(
            'key.json')
        self.client = speech.SpeechClient(credentials=self.credentials)
        # Audio file to be transcribed from google cloud bucket
        self.gcs_uri = URI
        self.audio = speech.RecognitionAudio(uri=self.gcs_uri)
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            language_code="en-US",
            audio_channel_count=2,
            enable_separate_recognition_per_channel=True,
        )

    def transcribe(self):
        transcript = ''

        # Detects speech in the audio file
        operation = self.client.long_running_recognize(
            config=self.config, audio=self.audio)
        start_time = time.time()
        print("Waiting for operation to complete...")
        response = operation.result()

        for result in response.results:
            transcript += result.alternatives[0].transcript
        print('Transcribing completed')
        print(f'Transcription took {time.time()-start_time}seconds')

        #Writing transcript into text file
        print('saving transcript')
        with open('transcript-3.txt', 'w') as file:
            file.write(transcript)
        

zoom_project = AudioTranscriber("gs://zoom_project_data/audio-3.flac")
transcript = zoom_project.transcribe()

#TODO:
# Add the 3 different transcript

#FIXME:
#The new line cleaning


