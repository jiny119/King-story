import streamlit as st
from gtts import gTTS
import os

# Streamlit UI
st.title("اردو کہانی جنریٹر + وائس اوور AI")

# User input
story_title = st.text_input("کہانی کا عنوان درج کریں:")

if st.button("کہانی بنائیں"):
    if story_title.strip():
        # AI-based simple story generation (Replace this with a real AI model)
        story = f"{story_title} کی کہانی شروع ہوتی ہے ایک خوبصورت جگہ پر جہاں حیرت انگیز واقعات رونما ہوتے ہیں۔"

        # Display story
        st.subheader("بنائی گئی کہانی")
        st.write(story)

        # Generate voiceover in Urdu
        tts = gTTS(text=story, lang='ur')
        audio_file = "story.mp3"
        tts.save(audio_file)

        # Play audio in Streamlit
        st.audio(audio_file, format="audio/mp3")

        # Option to download
        with open(audio_file, "rb") as file:
            st.download_button("وائس اوور ڈاؤن لوڈ کریں", file, file_name="story.mp3")

    else:
        st.error("براہ کرم کہانی کا عنوان درج کریں!")
