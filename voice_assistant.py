import json
from typing import Optional

import pyttsx3
import requests
import speech_recognition as sr
from rich.console import Console
from rich.markdown import Markdown

########################## Configuration ############################
API_KEY = "..." # Get it from https://console.groq.com/keys
#####################################################################

console = Console()

def generate_groq_prompt(prompt: str, model: str="llama3-70b-8192") -> Optional[str]:
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        data = {
            "model": model,
            "messages": [{'role': 'user', 'content': prompt}],
            "max_tokens": 2048,
            "n": 1,
            "temperature": 0.3,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            response = response_data['choices'][0]['message']['content']

            return response
        else:
            return
    except:
        return

def speak(text: str) -> None:
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()

def voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        console.print(Markdown("- Listening..."), style='cyan')

        try:
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='en-in')
            console.print(Markdown(f"- User: {text}"), style='yellow')
            return text
        except sr.UnknownValueError:
            speak("I didn't Undestand")
        except sr.RequestError as e:
            speak("I'm having trouble interacting with you. We'll get back later.")

console.print(Markdown(f'- Virtual Assistant Initialized Successfully..!'), style='magenta')
speak('Hello! How can I help you?')

while True:
    assistant_response = generate_groq_prompt(voice_input())
    
    if assistant_response:
        speak(assistant_response)
    else:
        speak("I'm sorry, I couldn't generate a response.")
