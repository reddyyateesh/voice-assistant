# Voice Assistant

This project is a simple voice assistant that listens to voice input, generates a response using the Groq API, and speaks the response back to the user.

## Features

- **Voice Input**: Captures voice input from the user.
- **Groq API Integration**: Sends the captured voice input to the Groq API to generate a response.
- **Text-to-Speech**: Speaks the response back to the user.

## Requirements

- Python 3.6+
- `requests`
- `pyttsx3`
- `speech_recognition`
- `rich`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/reddyyateesh/voice-assistant.git
    cd voice-assistant
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Get an API key from [Groq](https://console.groq.com/keys).
2. Replace the `API_KEY` variable in the code with your API key.

## Usage

Run the script:

```sh
python voice_assistant.py
```

The assistant will initialize and prompt you to speak. It will capture your voice input, send it to the Groq API, and speak the generated response back to you.

## Code Explanation

- Initialization:
    - `console = Console()`: Initializes a console for rich text output.
    - `speak(text: str) -> None`: Converts text to speech using `pyttsx3`.
    - `voice_input()`: Captures voice input using the `speech_recognition` library.

- Groq API Integration:
    - `generate_groq_prompt(prompt: str, model: str="llama3-70b-8192") -> Optional[str]`: Sends the prompt to the Groq API and returns the generated response.

- Main Loop:
    - The assistant continuously listens for voice input, generates a response using the Groq API, and speaks the response.

## Example

```txt
- Virtual Assistant Initialized Successfully..!
Assistant: Hello! How can I help you?
- Listening...
User: What's the weather like today?
Assistant: I'm sorry, I couldn't generate a response.
```

## License

This project is licensed under the MIT [License](LICENSE).

## Acknowledgments

- The Groq API for providing the AI model.
- The developers of `pyttsx3`, `speech_recognition`, and `rich` for their awesome libraries.
