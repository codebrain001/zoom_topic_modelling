import csv

# Imports the Google Cloud client library
from google.cloud import speech
# Import the google service account api authentication
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('key.json')

client = speech.SpeechClient(credentials=credentials)

# The name of the audio file to transcribe from cloud bucket
gcs_uri = "gs://zoom_project_data/audio.flac"
# gcs_uri = "gs://zoom_project_data/test.flac"

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    language_code="en-US",
)

transcript = ''

# Detects speech in the audio file
operation = client.long_running_recognize(config=config, audio=audio)
print("Waiting for operation to complete...")
response = operation.result()

# with open('text.csv', 'w') as file:
#     writer = csv.writer(file)
#     # create header
#     writer.writerow(['text'])
#     for result in response.results:
#         writer.writerow([result.alternatives[0].transcript])
    # The first alternative is the most likely one for this portion.
    #print(u"Transcript: {}".format(result.alternatives[0].transcript))
    

for result in response.results:
    transcript += result.alternatives[0].transcript
print('Transcribing completed')

f = open("transcript.txt", "w")
f.write(transcript)
f.close()


# f = open('text.csv','w')
# w = csv.writer(f, delimiter='.')
# # create header
# w.writerow(['text'])
# w.writerows([x.split('.') for x in transcript])
# f.close()

# print(transcript)

# print(u"Transcript: {}".format(result.alternatives[0].transcript))
# print("Confidence: {}".format(result.alternatives[0].confidence))
# print('Done')
