# AI Personal Assistant

## Overview
This AI Personal Assistant is a versatile voice-controlled application designed to perform a variety of tasks such as telling the time, playing music, opening apps, managing tasks (add/delete), sending messages, taking screenshots, and interacting with popular websites like YouTube and Instagram. It also incorporates conversational AI capabilities using Hugging Face's DialoGPT model.

## Features
- **Voice Interaction:** Voice commands to interact with the assistant using `speech recognition`.
- **Time and Date Reporting:** Retrieve current time and date.
- **Music Playback:** Play music via YouTube with a search function or random song selection.
- **Task Management:** Add, delete, and view tasks via a to-do list.
- **Social Media Access:** Open websites like YouTube and Instagram directly.
- **Screenshot Functionality:** Capture and save screenshots with timestamps.
- **AI Conversations:** Implement conversational AI using Hugging Face's DialoGPT (requires paid API for advanced functionality).
- **Notifications:** Display task-related notifications on your desktop.

## Technologies Used
- **Python**: Core language used for the assistant's development.
- **Libraries**:
  - `pyttsx3`: Text-to-speech functionality for communication.
  - `speech_recognition`: Convert speech into text.
  - `pyautogui`: Automate keyboard and mouse actions.
  - `pywhatkit`: Send messages on WhatsApp.
  - `wikipedia`: Search Wikipedia for information.
  - `transformers` (Hugging Face): For implementing conversational AI.
  - `youtubesearchpython`: Search and play YouTube videos.
  - `plyer`: For displaying notifications.
  - `requests`: For API requests.
  - `smptlib`, `ssl`: For email and SMS-related functionalities.

## Setup
1. Clone the repository:
git clone https://github.com/yourusername/AI-Assistant.git

markdown
Copy code
2. Install dependencies:
pip install -r requirements.txt

markdown
Copy code
3. Create a `user_config.py` file and set your API tokens (like Hugging Face and Gmail credentials for email functionalities).

4. Run the assistant:
python main.py

vbnet
Copy code

## Usage
Once the assistant is running, you can interact with it through voice commands like:
- "Hello" to wake up the assistant.
- "Play music" to start playing a random or searched song from YouTube.
- "Tell me the time" to get the current time.
- "Add a task" to add a new task to the to-do list.
- "Open YouTube" to open YouTube in your browser.
- "Take a screenshot" to capture your screen.
- "Tell me [something]" to get a conversational response from the AI (via Hugging Face's DialoGPT model).

## Limitations
- The conversational AI requires a paid Hugging Face API subscription for advanced functionality.
- Some features like sending emails may not work due to 2FA (Two-Factor Authentication) restrictions in email services.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
