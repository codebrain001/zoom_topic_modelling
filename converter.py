import pydub
class Converter:
    def __init__(self, audio_path):
        self.audio = pydub.AudioSegment.from_file(audio_path)

    def convert(self, desired_format):
        output = './audio.'+ desired_format
        self.audio.export(output, format=desired_format)
        print('Successfully completed conversion')
