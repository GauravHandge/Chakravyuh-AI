# Chakravyuh-AI
Strategic Chatbot Application

## Overview
Chakravyuh AI is a strategic chatbot application leveraging LangChain and Groq models to provide intelligent and insightful conversational experiences. The application is designed with advanced customization options, including selectable language models, conversational memory length, and engaging UI elements such as a background image and audio.

## Features
- **Interactive Conversations:** Engage with a chatbot powered by Groq's advanced models.
- **Customizable Memory Length:** Adjust the conversational memory length to suit your needs.
- **Dynamic UI Elements:** Includes background images and audio to enhance user interaction.
- **Model Selection:** Choose from various Groq-supported models.

## Prerequisites
Ensure you have the following installed and configured:

1. **Python 3.8 or later**
2. **pip** (Python package manager)


## Environment Setup
Create a `.env` file in the project directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

## Running the Application
1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open the provided URL in your browser to access Chakravyuh AI.

## Customization
### Background Image
To customize the background image:
- Replace the `background_image_url` variable in the `main()` function with your desired image URL.

### Background Audio
To change the background audio:
- Replace the `audio_url` variable in the `play_background_audio()` function with your audio URL.

### Supported Models
Add or modify the models in the sidebar dropdown by editing the `model` list in the `main()` function.

## Project Structure
```
.
├── app.py                # Main application file
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables (API key)
└── README.md             # Project documentation
```

## Dependencies
The project uses the following Python libraries:
- `streamlit`: For the web application interface
- `langchain`: For conversational AI capabilities
- `langchain_groq`: To interface with Groq models
- `python-dotenv`: For managing environment variables

## Usage
1. Launch the application using `streamlit run app.py`.
2. Use the sidebar to select a model and adjust memory length.
3. Ask questions in the text input area and get intelligent responses from Chakravyuh AI.

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests to improve the project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- **Streamlit:** For the interactive web application framework.
- **LangChain:** For the conversational AI backbone.
- **Groq:** For the powerful AI models.
