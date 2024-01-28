from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

"""
Script Name: Prince_ChatCot
Author: Prince Raj
Date: January 28, 2024
Description: The Python code is a Flask web application using OpenAI GPT-3.5 Turbo to create a chatbot, with routes for home ("/") and chatbot responses ("/get").
"""

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "Hello, I'm a Presonal Chatbot Created By Prince Raj. How can I help you?"}]

def get_chatbot_response(query):
    messages.append({"role": "user", "content": query})

    try:
        chat_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=messages,
            temperature=0.75,  
            max_tokens=1400,  
            stop=None,  
        )

        chatbot_response = chat_response.choices[0].message.content
        messages.append({"role": "assistant", "content": chatbot_response})
        return chatbot_response

    except openai.error.RateLimitError as e:
        return "Rate limit exceeded. Please wait for your quota to reset or upgrade your plan. More information: {}".format(e)

    except openai.error.OpenAIError as e:
        return "An error occurred: {}".format(e)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    response = get_chatbot_response(query)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321)
