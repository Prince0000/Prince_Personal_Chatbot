
# Prince_Personal_Chatbot

## Overview
**Script Name:** Prince_Personal_Chatbot  
**Author:** Prince Raj  
**Date:** January 28, 2024  
**Description:** Prince_Personal_Chatbot is a Python script utilizing Flask and OpenAI GPT-3.5 Turbo to create a personalized chatbot. It includes routes for the home ("/") page and chatbot responses ("/get").

## Prerequisites
- Python 3.x
- Flask
- OpenAI GPT-3.5 Turbo API key
- dotenv

## Setup
1. Install required dependencies by executing:  
   ```bash
   pip install Flask openai python-dotenv
   ```
2. Optionally, set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. Create a file named `.env` in the project directory and add your OpenAI GPT-3.5 Turbo API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
1. Run the Flask application:
   ```bash
   python <script_name.py>
   ```
2. Access the chatbot through your browser at `http://localhost:54321`.

## Routes
- **Home ("/")**: Displays the home page.  
- **Chatbot Responses ("/get")**: Accepts user queries via the `msg` parameter and returns the corresponding chatbot response.

## Chatbot Functionality
- Employs OpenAI GPT-3.5 Turbo for conversational responses.
- Initiates the conversation with the system message: "Hello, I'm a personalized chatbot. How can I assist you?"
- User messages become part of the conversation history, influencing subsequent chatbot responses.
- Handles OpenAI rate limit errors and other potential errors.

## Integrated Voice Command and Text-to-Speech
- Voice Command: The chatbot includes an integrated voice command feature.
- Text-to-Speech Options: Text-to-Speech options are available for enhancing user interaction.

## Notes
- Securely store your OpenAI API key in the `.env` file.
- Personalize the chatbot's initial message and parameters as needed.
- Exercise caution with sensitive information, especially when deploying the application.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

## Issues
Feel free to submit issues and enhancement requests.

# Social Media Accounts
[![Instagram](https://img.icons8.com/fluent/40/000000/instagram-new.png)](https://www.instagram.com/i.am_prince05?igsh=MW5leDEzMWxscmthZg==)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
[![Linkedin](https://img.icons8.com/fluent/40/000000/linkedin.png)](https://www.linkedin.com/in/prince-raj-0774911b1)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

