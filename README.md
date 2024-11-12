# YouTube Chat Chrome Extension with AI-powered Chatbot

This project is a Chrome extension that integrates a YouTube chat feature with an AI-powered chatbot using **Python Flask** as the backend and **Gemini AI** for answering questions. The chatbot provides an interactive experience for YouTube users by answering their queries in real-time within the chat interface.

## Features

- Real-time chat support in YouTube comments section.
- Integration with Gemini AI to provide accurate and relevant answers.
- Python Flask-based backend to handle API requests and responses.
- Chrome extension for a seamless YouTube chat interface experience.

## Installation

### 1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/youtube-chat-extension.git
cd youtube-chat-extension

### 2. Set Up the Backend

Prerequisites:
Python 3.7 or higher
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Running the Flask Server:
Make sure you have set up the .env file with the appropriate API keys for Gemini AI and any other environment-specific configurations.

bash
Copy code
python app.py
The Flask server will run at http://localhost:8000. Make sure your backend is running before loading the extension.

### 3. Set Up the Chrome Extension
Load the Extension in Chrome:
Open Chrome and go to chrome://extensions/.
Enable Developer mode (toggle in the top right corner).
Click Load unpacked and select the extension/ folder inside this project.
### 4. Configure the .env File
In the project directory, create a .env file and set the following environment variables:

makefile
Copy code
GEMINI_API_KEY=your_gemini_api_key
### 5. Usage
Once the extension is loaded and the Flask backend is running, visit any YouTube video with a live chat.
Open the chat window and interact with the AI chatbot to get responses to your queries.
Contributing
Feel free to fork this project, open issues, or submit pull requests for any improvements or bug fixes. Contributions are always welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Gemini AI for providing powerful AI capabilities.
Flask for creating the backend.
Chrome Extensions Documentation for helping create the Chrome extension interface.
