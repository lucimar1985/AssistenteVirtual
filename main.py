from numpy import source
import openai
import pyttsx3
import speech_recognition as sr

# set openai api key
openai.api_key = "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"

# initialize the text-to-speech engine
engine = pyttsx3.init()

# set the voice to a portuguese voice
engine = pyttsx3.init()
portuguese_voice = None
voices = engine.getProperty('voices')
portuguese_voice = None
for voice in voices:
    if 'pt-br' in voice.languages:
        portuguese_voice = voice
        break

if portuguese_voice is not None:
    engine.setProperty('voice', portuguese_voice.id)
else:
    print("Não foi encontrada nenhuma voz em português")

def transcrible_audio_to_text(filename):
    recognizer = sr.Recognizer()
    audio = recognizer.listen(source, timeout=None)
    try:
        return recognizer.recognizer.google(audio)
    except:
        print('skipping uknown error')


def generate_response(pronpt):
    # faça a solicitação à API do OpenAI
    response = openai.completion.create(
    engine="text-davinci-003",
    prompt=pronpt,
    max_tokens=4000,
    n=1,
    stop=None,
    temperature=0.5
)
    return response['choices'][0]['text']


# Imprima as respostas geradas pelo modelo de audio
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

    def main():
        while True:
            print("digite'genius'para começar a gravar sua pergunta")
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                audio = recognizer.listen(source)
                try:
                    trascription = recognizer.recognize_google(audio, language="pt-BR")
                    # record audio
                    filename = "input.wav"
                    print("faça sua pergunta...")
                    with sr.Microphone() as source:
                        recognizer = sr.recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, Timeout=None)
                        with open(filename,"wb") as f:
                            f.write(audio.get_wav_data())

                    # Transfira audio para formato testo
                            
                            text= transcrible_audio_to_text(filename)
                            if text:
                                print(f"Vc disse{text}")
                                # Gerar resposta usando chat gpt
                                response = generate_response(text)
                                print(f"Gpt Disse {text}")
                                # ler resposta usando texto_to_speech
                                speak_text(response)
                except Exception as e:
                    print("Ocorreu um erro: {}".format(e))

if __name__ == "__main__":
    main()