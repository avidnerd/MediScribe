import streamlit as st
import whisper
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
from io import BytesIO
import soundfile as sf
import ollama
import sqlite3
import logging

st.set_page_config(page_title="Record Visit", page_icon="🎤")

# Set up logging
logging.basicConfig(level=logging.DEBUG)

try:
    ollama.pull('llama2')
except Exception as e:
    st.error(f"Failed to pull llama2 model: {e}")
    logging.exception("Failed to pull llama2 model")

# Database setup
conn = sqlite3.connect('visits.db')
c = conn.cursor()

def convert_wav_to_mp3(input_wav_bytes):
    with BytesIO(input_wav_bytes) as wav_io:
        audio = AudioSegment.from_file(wav_io, format="wav")
        mp3_bytes = BytesIO()
        audio.export(mp3_bytes, format="mp3")
    return mp3_bytes

def save_visit(audio, transcript, summary):
    c.execute('INSERT INTO visits (audio, transcript, summary) VALUES (?, ?, ?)', (audio, transcript, summary))
    conn.commit()

st.title("Record Your Visit")

st.write("Record your visit:")
audio_file = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording", format="wav", key='recorder')

result_txt = ""
summary_txt = ""

if audio_file is not None:
    st.audio(audio_file['bytes'])
    try:
        with open("debug.wav", "wb") as debug_file:
            debug_file.write(audio_file['bytes'])

        audio_data, samplerate = sf.read(BytesIO(audio_file['bytes']))

        mp3_bytes = convert_wav_to_mp3(audio_file['bytes'])

        with open('output.mp3', 'wb') as f:
            f.write(mp3_bytes.getbuffer())

        model = whisper.load_model("base")
        initial_prompt = "Let's talk about Tylenol, Benadryl, Pepto-Bismol, Nyquil, Acetaminophen, and VapoRub."
        with st.spinner("Transcription in progress..."):
            result = model.transcribe('output.mp3')
            result_txt = result['text']
        st.success("Transcription completed!")
        with st.expander("Transcript", True):
            st.write(result["text"])
    except Exception as e:
        st.error(f"An error occurred during audio processing: {e}")
        logging.exception("An error occurred during audio processing")
else:
    st.write("No audio recorded yet. Please record your voice.")

if result_txt != "":
    try:
        with st.spinner("Summarization in progress..."):
            finalbulletpoints = ollama.generate(model='llama2', prompt='Based on this doctor-patient conversation, describe the patient symptoms, the doctor diagnosis, and the actions that the patient needs to take. Here is the conversation ' + str(result_txt))
        summary_txt = finalbulletpoints['response']
        st.success("Summarization completed!")
        with st.expander("Summary of your Visit", True):
            st.write(summary_txt)
        save_visit(audio_file['bytes'], result_txt, summary_txt)
    except Exception as e:
        st.error(f"An error occurred during summarization: {e}")
        logging.exception("An error occurred during summarization")

conn.close()
