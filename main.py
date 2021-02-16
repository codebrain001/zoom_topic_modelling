from converter import Converter
from transcribe import Transcriber
from sentence-split import Spliter
from modeling import LdaModeling

def main()


if __name__ == '__main__':
    audio_converter = Converter('./audio.mp3')
    audio_converter.convert('flac')
    zoom_project = Transcriber("gs://zoom_project_data/audio.flac")
    transcript = zoom_project.transcribe()
    sentence_spliter = Spliter.split()
    lda_instance = LdaModeling('transcript.csv')
    gensim_corpus, gensim_dictionary = lda_instance.preprocessing()
    lda_model = lda_instance.modeling()
    lda_instance.plotting(lda_model, gensim_corpus, gensim_dictionary)
    lda_instance.performance(lda_model, gensim_corpus, gensim_dictionary)
    

main()